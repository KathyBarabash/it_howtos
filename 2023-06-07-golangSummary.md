## TODO
Writing Web Applications https://go.dev/doc/articles/wiki/

## Sources

### Official 
Style guide https://go.dev/doc/effective_go 

### DigitalOcen

https://www.digitalocean.com/community/tutorial_series/how-to-code-in-go 

 fmt.Printf("%d. Sources:", section)
        fmt.Println("   https://www.digitalocean.com/community/tutorial_series/how-to-code-in-go stopp
ed working for me, maybe registration is required")
        fmt.Println("   https://zetcode.com/all/#go     maybe good but disordered topics")
        fmt.Println("   https://www.w3schools.com/go/   very basic but good for starters")
        fmt.Println("   https://www.programiz.com/golang some advanced info (goroutines, channels, sel
ect) but seems to have many errors")
        fmt.Println("   https://gobyexample.com/    xxx")
        fmt.Println("   https://go.dev/doc/tutorial/    xxx")
        fmt.Println("   https://www.geeksforgeeks.org/golang-tutorial-learn-go-programming-language/
  xxx")
        fmt.Println("   https://riptutorial.com/go    xxx")
        fmt.Println("   https://www.javatpoint.com/go-tutorial    xxx")
        fmt.Println("   https://golangbot.com/learn-golang-series/    xxx")
        fmt.Println("       xxx")
        fmt.Println("---------")

### LinkedIn courses

## Go Essential Training by Miki Tebeka 
Date: 2023-05-15
Link: https://www.linkedin.com/learning/go-essential-training-16567666
Code: https://github.com/LinkedInLearning/go-essential-training-2446262
Learnt:

Basic structure
```
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Welcome Gophers ☺")
}
```

Naming: upper case for public, lower case for private entities

Printing and formatting with fmt package 
Print, Println, Printf  
        %v for value
        %T for type
Sprint, Sprintln, Sprintf
        s := fmt.Sprintf("%d", n)       convert integer to string
Errorf
        error built-in type

Arrays, also called slices
        <slice_name> := []<element_type>{<comma_separated_values>}

        loons := []string{"bugs", "daffy", "taz"}

        for i, name := range loons {
		fmt.Printf("%s at %d\n", name, i)
	}

        loons = append(loons, "elmer")

        len(loons)                      to get size

Maps
        <map_name> := map[<key_type>]<value_type>{<comma_separated_kv_pairs>}

        stocks := map[string]float64{
		"AMZN": 2087.98,
		"GOOG": 2540.85,
		"MSFT": 287.70, // Must have trailing comma in multi line
	}

        value, ok := stocks["TSLA"]             // to check/get
        stocks["TSLA"] = 822.12                 // to add
	delete(stocks, "AMZN")                  // to delete, even if not there

String manipulation with strings package
        words := strings.Fields(text)           // tokenize with white space
        strings.ToLower(word)                   // case

Functions
        func <name> (<param1_name> <param1_type>, <param2_name> <param2_type>) (<result1_name> <result1_type>, <result2_name> <result2_type>) {
                //body
                //parameters are copied
        }

Accessing web with net/http pckage
        func contentType(url string) (string, error) {
	resp, err := http.Get(url)
	if err != nil {
		return "", err
	}

	defer resp.Body.Close() // Make sure we close the body

	ctype := resp.Header.Get("Content-Type")
	if ctype == "" { // Return error if Content-Type header not found
		return "", fmt.Errorf("can't find Content-Type header")
	}

	return ctype, nil
}

Measuring and displaying time with time package
        time.Time       // type to hold time
        time.Duration   // type to hold duration
        time.Now()      // function to return current time
        func (t Time) Add(d Duration) Time
        func (t Time) Hour() int //returns the hour within the day specified by t, in the range [0, 23]

Custom types (structures) and methods
        type Budget struct {
                CampaignID string
                Balance    float64 // USD
                Expires    time.Time
        }
        b1 := Budget{"Kittens", 22.3, time.Now().Add(7 * 24 * time.Hour)}
        var b2 Budget   //with empty fields

        // method that does not modify the structure
        func (b Budget) TimeLeft() time.Duration {
	        return b.Expires.Sub(time.Now().UTC())
        }       

        // method that needs to modify the structure
        func (b *Budget) Update(sum float64) {
                b.Balance += sum
        }

        //constructor
        func NewBudget(campaignID string, balance float64, expires time.Time) (*Budget, error) {
                //check inputs and do stuff
                b := Budget{
                        CampaignID: campaignID,
                        Balance:    balance,
                        Expires:    expires,
                }
                return &b, nil
        }
```

```
[%v for value, %T for type], Sprintf, Errorf
- 

## Installing

## Basic working installation for Ubuntu
```
>: sudo apt install golang-go
>: which go
/usr/bin/go
>: go version
go version go1.13.8 linux/amd64
>: go help
```
This won't create GOPATH and GOROOT variables



