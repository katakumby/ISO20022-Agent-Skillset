---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.1 Account", "12.1.1.3 SecuritiesAccount19"]
file_pages: [375]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.1.3 SecuritiesAccount19

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 375 to 375.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 375

```text
12.1.1.3  SecuritiesAccount19
Definition: Account to or from which a securities entry is made.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 375
   Type <Tp> [0..1] ± 375
   Name <Nm> [0..1] Text 375
12.1.1.3.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: Max35Text on page 493
12.1.1.3.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains the following elements (see GenericIdentification30 on page 400 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
12.1.1.3.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: Max70Text on page 493
12.1.2 Account Identification
12.1.2.1  AccountIdentification26
Definition: Unique identifier of an account, as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Proprietary <Prtry> [1..1]  376
     Identification <Id> [1..1] Text 376
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 375
```

