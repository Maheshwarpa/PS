from bs4 import  BeautifulSoup
import requests
import csv

# method to scrap data
def scrap(soup,c,a):
    #fetching data
    try:
        title=soup.find('h1',class_='lh-copy dark-gray mv1 f3 mh0-l mh3 b').text
        rating=soup.find('span',class_='f-headline b').text
        cost=soup.find('span', class_='inline-flex flex-column').text
        print(title)
        print(cost)
        if(rating[0].isdigit()==True):
            ra=rating[:3]
        else:
            ra=""
        print(ra)
        List=[title.strip(),ra,cost,"https://www.walmart.com"+a]
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
    URL = "https://www.walmart.com"
    departments = {
        "Electronics" : "https://www.walmart.com/cp/electronics/3944?povid=GlobalNav_rWeb_Electronics_Electronics_ShopAll",
        # "clothing" : "https://www.amazon.com/amazon-fashion/b/ref=dp_bc_aui_C_1?ie=UTF8&node=7141123011"
    }
    subsections=list(departments.keys())

    # # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")
    linkedlist=[]

    classname=['no-underline sans-serif flex flex-column items-center']
    #getting links from each department logic.
    for i in range(0,len(classname)):
        a=pullLinks(departments[subsections[i]],classname[i])
        linkedlist.append(a)
    print(linkedlist)
    count = 0;
    # for j in range(0,len(linkedlist)):
    #     for k in range(0,len(linkedlist[j])):
    #         a = URL + linkedlist[j][k]
    #         links_list = pullLinks(a, "absolute w-100 h-100 z-1 hide-sibling-opacity")
    #         #page navigation logic
    #         for i in range(1, 5):
    #         # a = URL + linkedlist[0][0]
    #             items = a + '&page=' + str(i)
    #             links_list=pullLinks(a, "absolute w-100 h-100 z-1 hide-sibling-opacity")
    #
    #         print('Started')
    #         for link in links_list:
    #             if (link.startswith("https")):
    #                 webpage1=requests.get(link,headers=HEADERS)
    #             else:
    #                 webpage1 = requests.get("https://www.walmart.com" + link,headers=HEADERS)
    #             new_soup = BeautifulSoup(webpage1.content, "html.parser")
    #             scrap(new_soup, count,link)
    #
    #             count = count + 1
    #             print()
    #             print("finish", count)



