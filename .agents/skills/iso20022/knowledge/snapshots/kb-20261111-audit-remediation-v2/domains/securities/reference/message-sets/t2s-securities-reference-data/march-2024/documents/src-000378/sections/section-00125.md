---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.2 Option <Optn>", "13.1.2.2.2.11 VersionNumber <VrsnNb>"]
file_pages: [183]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.2.11 VersionNumber <VrsnNb>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 183 to 183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 183

```text
Definition: Assignment method expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.2.2.11  VersionNumber <VrsnNb>
Presence: [0..1]
Definition: Number allocated by options exchanges to record that an option has undergone a change in
its contract specifications (particularly adjustment of the strike price).
Datatype: "Number" on page 532
13.1.2.2.2.12  ExpiryLocation <XpryLctn>
Presence: [0..1]
Definition: Financial center where option expires.
Datatype: "Max4AlphaNumericText" on page 534
13.1.2.2.2.13  Standardisation <Stdstn>
Presence: [0..1]
Definition: Specifies whether the terms of the security (underlying instruments, expiration date, contract
size) are defined according to the exchange specifications or whether they can be user defined.
Standardisation <Stdstn> contains one of the following Standardisation3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..*] CodeSet 183
Or}   Proprietary <Prtry> [1..1] ± 184
13.1.2.2.2.13.1  Code <Cd>
Presence: [1..*]
Definition: Standardisation expressed as an ISO 20022 code.
Datatype: "Standardisation1Code" on page 524
CodeName Name Definition
FLEX Flexible Derivatives defined according to
exchange specifications, but certain
characteristics can be user defined.
NSTA NonStandardised Custom-made instrument between two
parties. Underlying
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 183 March 2024
```

