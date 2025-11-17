'''You are building a basic dashboard for a blog website. The blog has a list that stores the number of views for different blog posts.
Your task is to:
Loop through the given list of blog post views.
For each blog post:
If views > 1000, print "Trending"
If views between 500 and 1000, print "Average"
If views < 500, print "Low Traffic"
After the loop:
Print the total number of views
Print how many posts were "Trending"
Use this list for blog views:
blog_views = [150, 800, 2500, 600, 1200, 450, 3000]'''
blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
for views in blog_views:
  if views > 1000:
    print("Trending")
  elif views >= 500 and views <= 1000:
      print("Average")
  else:
      print("Low traffic")
total = 0
trending_count = 0

for views in blog_views:
    total += views
    if views >= 1000:
        trending_count += 1
print("Total views ",total)
print("Number of trending posts:", trending_count)


      
