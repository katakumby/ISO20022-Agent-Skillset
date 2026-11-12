---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.16 Identification Information", "7.1.16.1 TransactionIdentifications55", "7.1.16.1.11 RelatedTransactionIdentification <RltdTxId>"]
file_pages: [349]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.16.1.11 RelatedTransactionIdentification <RltdTxId>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 349 to 349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 349

```text
7.1.16.1.11  RelatedTransactionIdentification <RltdTxId>
Presence: [0..1]
Definition: Matching reference
Datatype: "Max35Text" on page 557
7.1.16.2  GenericIdentification80
Definition: Identification expressed as a proprietary type and narrative description.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 349
   Identification <Id> [0..1] Text 349
7.1.16.2.1  Type <Tp>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 352 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.16.2.2  Identification <Id>
Presence: [0..1]
Definition: Name or number assigned by an entity to enable recognition of that entity.
Datatype: "Max35Text" on page 557
7.1.16.3  IdentificationType42Choice
Definition: Choice between a code and a data source scheme to specify the type of alternate
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 349
Or}   Proprietary <Prtry> [1..1] ± 350
7.1.16.3.1  Code <Cd>
Presence: [1..1]
Definition: Type of identification is defined using a code.
Datatype: "TypeOfIdentification1Code" on page 547
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 349 March 2026
```

