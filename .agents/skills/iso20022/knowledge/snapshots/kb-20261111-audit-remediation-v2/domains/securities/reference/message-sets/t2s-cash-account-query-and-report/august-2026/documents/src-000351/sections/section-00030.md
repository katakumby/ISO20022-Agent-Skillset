---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>", "2.4.5.20 StatementFrequencyAndFormat <StmtFrqcyAndFrmt>", "2.4.5.20.3 DeliveryAddress <DlvryAdr>"]
file_pages: [34]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5.20.3 DeliveryAddress <DlvryAdr>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 34 to 34.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 34

```text
Datatype: "Max35Text" on page 183
2.4.5.20.3  DeliveryAddress <DlvryAdr>
Presence: [1..1]
Definition: Specifies the delivery address for statements.
Datatype: "Max350Text" on page 183
2.4.5.20.4  Format <Frmt>
Presence: [1..1]
Definition: Specifies the format for statements.
Format <Frmt> contains one of the following CommunicationFormat1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 34
Or}   Proprietary <Prtry> [1..1] Text 34
2.4.5.20.4.1  Code <Cd>
Presence: [1..1]
Definition: Unique and unambiguous identification of communication format using a code list.
Datatype: "ExternalCommunicationFormat1Code" on page 176
2.4.5.20.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification of communication format using a proprietary
identification scheme.
Datatype: "Max35Text" on page 183
2.4.5.21  Restriction <Rstrctn>
Presence: [0..*]
Definition: Restriction on capability or operations allowed.
Restriction <Rstrctn> contains the following Restriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RestrictionType <RstrctnTp> [1..1]  35
{Or     Code <Cd> [1..1] Text 35
Or}     Proprietary <Prtry> [1..1] ± 35
   ValidFrom <VldFr> [1..1] DateTime 35
   ValidUntil <VldUntil> [0..1] DateTime 35
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 34 August 2026
```

