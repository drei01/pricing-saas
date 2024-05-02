# 1. Generate SEO pages

`python3 merge-csv-md.py --csv Tools-Grid.csv -o test.md -filename stripe-customer-portal template-customer-portal.md`

`python3 merge-csv-md.py --csv Tools-Grid.csv -o test.md -filename stripe-subscription template.md`

# 2. Download images
`python3 download-images.py Tools-Grid.csv`