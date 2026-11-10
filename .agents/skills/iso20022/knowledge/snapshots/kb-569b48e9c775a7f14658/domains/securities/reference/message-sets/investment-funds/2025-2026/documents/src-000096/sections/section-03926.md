---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.1 TaxReporting3", "66.1.47.1.5 CashAccountDetails <CshAcctDtls>", "66.1.47.1.5.6 AccountOwnerOtherIdentification <AcctOwnrOthrId>"]
file_pages: [5218]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.1.5.6 AccountOwnerOtherIdentification <AcctOwnrOthrId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5218 to 5218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5218

```text
AccountServicerBranch <AcctSvcrBrnch> contains the following elements (see "BranchData4" on
page 4482 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4482
   Name <Nm> [0..1] Text 4482
   PostalAddress <PstlAdr> [0..1] ± 4482
66.1.47.1.5.6  AccountOwnerOtherIdentification <AcctOwnrOthrId>
Presence: [0..*]
Definition: Alternative identification, for example, national registration identification number, passport
number, tax identification number. This may be an account number used to further identify the
beneficial owner, for example, a Central Provident Fund (CFP) account as required for Singapore.
AccountOwnerOtherIdentification <AcctOwnrOthrId> contains the following elements (see
"GenericIdentification82" on page 4541 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4541
   Type <Tp> [1..1]  4541
{Or     Code <Cd> [1..1] CodeSet 4541
Or}     Proprietary <Prtry> [1..1] ± 4542
   Issuer <Issr> [0..1] Text 4543
   IssueDate <IsseDt> [0..1] Date 4543
   ExpiryDate <XpryDt> [0..1] Date 4543
   State <Stat> [0..1] Text 4543
   IssuerCountry <IssrCtry> [0..1] CodeSet C12 4543
66.1.47.1.5.7  InvestmentAccountType <InvstmtAcctTp>
Presence: [0..1]
Definition: Type of account.
InvestmentAccountType <InvstmtAcctTp> contains one of the following elements (see
"AccountType2Choice" on page 4327 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4327
Or}   Proprietary <Prtry> [1..1] ± 4327
66.1.47.1.5.8  CreditDebit <CdtDbt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5218 May 2026
```

