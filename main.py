from bs4 import  BeautifulSoup
import requests
import csv

# method to scrap data
def scrap(soup,c,a):
    #fetching data
    try:
        title=soup.find('span',class_='a-size-large product-title-word-break').text
        # year=soup.find_all('td', class_='URwL2w col col-9-12')
        rating=soup.find('span',class_='a-icon-alt').text
        # reviews=soup.find('span',class_='_2_R_DZ').text
        # # actual_price=soup.find('span',class_='a-price a-text-price a-size-base').text
        # c=soup.find_all('td', class_='a-span3')
        # color=c.find('span',class_='a-size-base po-break-word').text
        cost=soup.find('span', class_='a-offscreen').text
        # picture_rating=soup.find_all('text',class_='_2Ix0io')
        # customer_review=soup.find_all('p',class_='_2-N8zT')
        # printing all the data
        print(title)
        # print(rating)
        # print(reviews)
        # print(color)
        # print(actual_price)
        print(cost)
        # overall_rating=''
        # for i in picture_rating:
        #     overall_rating=overall_rating+' '+i.get_text()
        # print(overall_rating.strip())
    #     cust_top_review=''
    #     for j in range(0,len(customer_review)):
    #         if j<3:
    #             cust_top_review=cust_top_review+','+customer_review[j].get_text()
    #     print(cust_top_review)
    #     a='';b='';c='';d='';e=''
    #     for i in range(0,len(year)):
    #         if i==3:
    #             a=year[i].get_text()
    #         elif i==10:
    #             b=year[i].get_text()
    #         elif i==28:
    #             c=year[i].get_text()
    #         elif i==29:
    #             d=year[i].get_text()
    #         elif i==59:
    #             e=year[i].get_text()
    #         else: continue
        if(rating[0].isdigit()==True):
            ra=rating[:3]
        else:
            ra=""
        print(ra)
        List=[title.strip(),ra,cost,"https://www.amazon.com"+a]
        if c==0:
            # fetching data into csv file
            with open('walmart_data.csv', 'w',encoding="utf-8",newline='') as f_object:
                writer_object = csv.writer(f_object)

                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(['Title','Rating','Cost','Links'])
                print('row inserted')
                # Close the file object
                f_object.close()
                return 0
        else:
            with open('walmart_data.csv', 'a',encoding="utf-8",newline='') as f_object:
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



