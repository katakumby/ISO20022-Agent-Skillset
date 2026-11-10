---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.2 Account Identification", "66.1.2.9 Account7"]
file_pages: [4337]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.2.9 Account7

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4337 to 4337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4337

```text
IdentificationAsDSS <IdAsDSS> contains the following elements (see "AccountIdentification3" on
page 4328 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4328
   Issuer <Issr> [1..1] Text 4328
   Information <Inf> [1..1] Text 4328
66.1.2.9  Account7
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4337
   AccountServicer <AcctSvcr> [0..1] ± 4337
66.1.2.9.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains the following elements (see "AccountIdentification1" on page 4328 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Proprietary <Prtry> [1..1] ± 4329
66.1.2.9.2  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Institution servicing an account and assigning the account identifier to the account owner.
AccountServicer <AcctSvcr> contains one of the following elements (see "PartyIdentification2Choice"
on page 4887 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4887
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4888
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4888
66.1.2.10  SubAccountIdentification3
Definition: Account to or from which a securities entry is made.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4337 May 2026
```

