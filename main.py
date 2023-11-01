from bs4 import  BeautifulSoup
import requests
import csv

# method to scrap data
def scrap(soup,c,a):
    #fetching data
    try:
        title=soup.find('span',class_='a-size-large product-title-word-break').text
        rating=soup.find('span',class_='a-icon-alt').text
        cost=soup.find('span', class_='a-offscreen').text
        # printing all the data
        print(rating)
        print(cost)
        t=title.split(",")[0]
        if(len(t)>1):
            t = t[0:t[0:40].rindex(" ")]
        print(t)
        if(rating[0].isdigit()==True):
            ra=rating[:3]
        else:
            ra=""
        print(ra)
        List=[t.strip(),ra,cost,"https://www.amazon.com"+a]
        if c==0:
            # fetching data into csv file
            with open('Amazon_data.csv', 'w',encoding="utf-8",newline='') as f_object:
                writer_object = csv.writer(f_object)

                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(['Title','Rating','Cost','Links'])
                print('row inserted')
                # Close the file object
                f_object.close()
                return 0
        else:
            with open('Amazon_data.csv', 'a',encoding="utf-8",newline='') as f_object:
                writer_object = csv.writer(f_object)

                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(List)
                print('row inserted')
    #             # Close the file object
                f_object.close()
                return 0
    except AttributeError:
        available = "Not Available"
        return available


# method to pull all the links
def pullLinks(URL,className):
    webpage2 = requests.get(URL, headers=HEADERS)
    soup2 = BeautifulSoup(webpage2.content, "html.parser")
    s_links = soup2.find_all("a", class_=className)
    print()
    links_list = []
    for link in s_links:
        links_list.append(link.get('href'))
    return links_list



if __name__ == '__main__':
    # Headers for request
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'Accept-Language': 'en-US'})

    # The webpage URL
    URL = "https://www.amazon.com"
    departments = {
        "Electronics" : "https://www.amazon.com/electronics-store/b/ref=dp_bc_aui_C_1?ie=UTF8&node=172282",
        "clothing" : "https://www.amazon.com/amazon-fashion/b/ref=dp_bc_aui_C_1?ie=UTF8&node=7141123011"
    }
    subsections=list(departments.keys())

    # # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")
    linkedlist=[]

    classname=['a-color-base a-link-normal','a-link-normal text-link']
    #getting links from each department logic.
    for i in range(0,len(classname)):
        a=pullLinks(departments[subsections[i]],classname[i])
        linkedlist.append(a)
    print(linkedlist)
    count = 0;
    for j in range(0,len(linkedlist)):
        for k in range(0,len(linkedlist[j])):
            a = URL + linkedlist[j][k]
            links_list = pullLinks(a, "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
            #page navigation logic
            for i in range(1, 5):
            # a = URL + linkedlist[0][0]
                items = a + '&page=' + str(i)
                links_list=pullLinks(a, "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")

            print('Started')
            for link in links_list:
                if (link.startswith("https")):
                    webpage1=requests.get(link,headers=HEADERS)
                else:
                    webpage1 = requests.get("https://www.amazon.com" + link,headers=HEADERS)
                new_soup = BeautifulSoup(webpage1.content, "html.parser")
                scrap(new_soup, count,link)

                count = count + 1
                print()
                print("finish", count)



