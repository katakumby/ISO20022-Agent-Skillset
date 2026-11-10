---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.1 Account", "66.1.1.3 AccountOpeningType1Choice", "66.1.1.3.2 Proprietary <Prtry>"]
file_pages: [4325]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.1.3.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4325 to 4325.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4325

```text
CodeName Name Definition
NEWA NewAccountOpening Account request is to open a new
account.
SUPA SupplementaryAccountOpening Account request is to open a
supplementary account, that is, based
on an existing account.
66.1.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of account opening instruction expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.1.4  Account23
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 4325
   RelatedAccountDetails <RltdAcctDtls> [0..1] ± 4325
66.1.1.4.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Identification of the account.
Datatype: "Max35Text" on page 5403
66.1.1.4.2  RelatedAccountDetails <RltdAcctDtls>
Presence: [0..1]
Definition: Information about the account to which the existing account is to be linked.
RelatedAccountDetails <RltdAcctDtls> contains the following elements (see "GenericIdentification1"
on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4325 May 2026
```

