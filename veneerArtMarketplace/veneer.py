'''
A marketplace for people and organizations to buy and sell pieces of
art, made by using python3 made by Rakesh Meena for Codecademy project.
'''

#Artworks description

class Art:
  def __init__(self,artist,title,year,medium,owner):
    self.artist=artist
    self.title=title
    self.medium=medium
    self.year=year
    self.owner=owner

  def __repr__(self):
    return "{name}, \" {title}\", {year}, {medium}, {owner_name}, {owner_loc}.\n".format(name=self.artist,
    	title=self.title,year=self.year,medium=self.medium,owner_name=self.owner.name,owner_loc=self.owner.location)


#Marketplace for buying and selling artworks

class Marketplace:
	def __init__(self):
		self.listings=[]

	def add_listing(self,new_listing):
		self.listings.append(new_listing)

	def remove_listing(self,expired_listing):
		self.listings.remove(expired_listing)

	def show_listings(self):
		for listing in self.listings:
			print(listing)


#Clients details

class Client:
	def __init__(self,name,location,is_museum):
		self.name=name
		self.is_museum=is_museum
		if is_museum:
			self.location=location
		else:
			self.location="Private Collection"

	def sell_artwork(self,artwork,price):
		if artwork.owner == self:
			new_listing = Listing(artwork,price,self)
			veneer.add_listing(new_listing)

	def buy_artwork(self,artwork):
		if artwork.owner != self:
			art_listing = None
			for listing in veneer.listings:
				if listing.art == artwork:
					art_listing=listing
					break
			if art_listing != None:
				art_listing.art.owner=self
				veneer.remove_listing(art_listing)

				
#Listings of artworks 

class Listing:
	def __init__(self,art,price,seller):
		self.art=art
		self.price=price
		self.seller=seller

	def __repr__(self):
		return "{name} is on sell for {price}.\n".format(name=self.art.title,price=self.price)
      

veneer=Marketplace()
#print(veneer.show_listings())

#Clients
edytta=Client("Edytta Halpirt", None, False)
moma=Client("THE MOMA", "New York", True)
 
#Artwork
girl_with_mandolin=Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas",edytta)
print(girl_with_mandolin)

#Seller
edytta.sell_artwork(girl_with_mandolin,"$6M (USD)")
veneer.show_listings()

#Buyer
moma.buy_artwork(girl_with_mandolin) print(girl_with_mandolin)