# This file will check the latest releases from the main branch and releases new images.

branch_name := Dev
side_branch := release
image_name := aes-clone-app
repo_name := hamzaping/aesclone
tag_name := v.2


# Fetch the latest releases from the a branch locally and remotly
branch-update:
	@echo "***\t Fetching from $(branch_name)\t***"
	@git fetch origin $(branch_name)
	@git merge origin/$(branch_name)
	@git push origin $(side_branch)
	@echo "***\t Finshed the fetching from $(branch_name)\t***"

# To build the new image of the script
build-image:
	cd docker;\
	docker build -t $(image_name) .

# To upload the new image remotly
push-image:
	cd docker;\
	docker image tag $(image_name) $(repo_name):$(tag_name)
	docker image push $(repo_name):$(tag_name)
