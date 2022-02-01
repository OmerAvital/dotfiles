# Signing commits

## 1. Download gpg-suite
```shell
$ brew install gpg-suit
```

## 2. Generate a gpg key
### Option 1: With GPG Keychain
Create the GPG Key by clicking the `+` in the GPG Keychain app.\
Check the manual directions to ensure that the settings are correct 

### Option 2: Manually
```shell
$ gpg --full-generate-key
```
    
a) Choose option 1: RSA and RSA\
b) Enter `4096` bits\
c) Enter time for key to expire (`enter` to not expire)\
d) Enter email (`76176305+OmerAvital@users.noreply.github.com`)\
e) Type a secure passphrase

## 3. Add the key to GitHub
### Get GPG key ID
#### Option 1: GPG Keychain
Open the GPG key by double-clicking on it and copy the key ID.

#### Option 2: Manual
a) List the keys
```shell
$ gpg --list-secret-keys --keyid-format=long
```

b) From the list of GPG keys, copy the long form of the GPG key ID you'd like to use.
In this example, the GPG key ID is `3AA5C34371567BD2`:
```shell
$ gpg --list-secret-keys --keyid-format=long
/Users/hubot/.gnupg/secring.gpg
------------------------------------
sec   4096R/3AA5C34371567BD2 2016-03-10 [expires: 2017-03-10]
uid                          Hubot 
ssb   4096R/42B317FD4BA89E7A 2016-03-10
```

### Add to GitHub
c) Use the command below, substituting in the GPG key ID you'd like to use, to copy the key to your clipboard.
In this example, the GPG key ID is `3AA5C34371567BD2`:
```shell
$ gpg --armor --export 3AA5C34371567BD2 | pbcopy
```

d) [Add the GPG key to your GitHub account][github-add-gpg-key].

## 4. Tell Git your signing key
a) [Get the GPG key ID][get-id].\
b) Paste the text below, substituting in the GPG key ID you'd like to use.
In this example, the GPG key ID is `3AA5C34371567BD2`:
```shell
$ git config --global user.signingkey 3AA5C34371567BD2
```
c) Tell git to always sign commits.
```shell
$ git config --global commit.gpgsign true
```

## Other resources
- [Github guide][guide]

[github-add-gpg-key]:
    https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-new-gpg-key-to-your-github-account
[get-id]:
    #get-gpg-key-id
[guide]:
    https://docs.github.com/en/authentication/managing-commit-signature-verification/
