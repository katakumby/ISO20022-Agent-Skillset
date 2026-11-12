---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.1 Account", "4.1.1.4 ProxyAccountIdentification1", "4.1.1.4.1 Type <Tp>", "4.1.1.4.1.1 Code <Cd>"]
file_pages: [44]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.1.4.1.1 Code <Cd>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 44 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 44

```text
Type <Tp> contains one of the following ProxyAccountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 44
Or}   Proprietary <Prtry> [1..1] Text 44
4.1.1.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalProxyAccountType1Code" on page 77
4.1.1.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 83
4.1.1.4.2  Identification <Id>
Presence: [1..1]
Definition: Identification used to indicate the account identification under another specified name.
Datatype: "Max2048Text" on page 82
4.1.1.5  SecuritiesAccount19
Definition: Account to or from which a securities entry is made.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 44
   Type <Tp> [0..1] ± 44
   Name <Nm> [0..1] Text 45
4.1.1.5.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: "Max35Text" on page 83
4.1.1.5.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
44 March 2024
```

