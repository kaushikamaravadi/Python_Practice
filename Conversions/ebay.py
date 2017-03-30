from xml.etree import ElementTree
import csv

keys = []
csv_file = open('ebay.csv', 'w')
field_names = ["seller_name", "seller_rating", "payment_type", "shipping_info", "current_bid", "time_left", "high_bidder", "num_items", "num_bids", "started_at", "bid_increment", "location", "opened", "closed", "id_num", "notes", "highest_bid_amount", "quantity", "memory", "hard_drive", "cpu", "brand", "description"]
writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=field_names)
writer.writeheader()
file_open = open('/home/ubuntu/Downloads/ebay.xml', 'rt')
tree = ElementTree.parse(file_open)
root = tree.getroot()
for listings in root.findall('listing'):
    for nodes in listings:
        for i in nodes.findall("seller_name"):
            values = {}
            # print(i.text.strip())
            values["seller_name"] = i.text.strip()
            # writer.writerow(values)
        for rating in nodes.findall("seller_rating"):
            print(rating.text)
            values["seller_rating"] = rating.text.strip()
        for payment in nodes.findall("current_bid"):
            print(payment.text)
            values["current_bid"] = payment.text.strip()
        for time_left in nodes.findall("time_left"):
            values["time_left"] = time_left.text.strip()
        for high in nodes.findall("high_bidder"):
            values["high_bidder"] = high.text.strip()
        for num in nodes.findall("num_items"):
            values["num_items"] = num.text.strip()
        for num_of_bids in nodes.findall("num_bids"):
            values["num_bids"] = num_of_bids.text.strip()
        for started in nodes.findall("started_at"):
            values["started_at"] = started.text.strip()
        for bid_inc in nodes.findall("bid_increment"):
            values["bid_increment"] = bid_inc.text.strip()
        for loc in nodes.findall("location"):
            values["location"] = loc.text.strip()
        for opened in nodes.findall("opened"):
            values["opened"] = opened.text.strip()
        for closed in nodes.findall("closed"):
            values["closed"] = closed.text.strip()
        for id_num in nodes.findall("id_num"):
            values["id_num"] = id_num.text.strip()
        for notes in nodes.findall("notes"):
            values["notes"] = notes.text.strip()
        for high_bid in nodes.findall("highest_bid_amount"):
            values["highest_bid_amount"] = high_bid.text.strip()
        for quan in nodes.findall("quantity"):
            values["quantity"] = quan.text.strip()
        for memory in nodes.findall("memory"):
            values["memory"] = memory.text.strip()
        for hard_drive in nodes.findall("hard_drive"):
            values["hard_drive"] = hard_drive.text.strip()
        for cpu in nodes.findall("cpu"):
            values["cpu"] = cpu.text.strip()
        for brand in nodes.findall("brand"):
            values["brand"] = brand.text.strip()
        for descr in nodes.findall("description"):
            values["description"] = descr.text.strip()
            writer.writerow(values)
