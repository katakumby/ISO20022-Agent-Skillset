---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2 Balance <Bal>", "2.4.2.2.2.1 Type <Tp>"]
file_pages: [15]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.2.1 Type <Tp>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 15 to 15.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 15

```text
Constraints
• CounterpartyIdentification1Rule
If at least one occurrence of CounterpartyType is present and is equal to Multilateral (MULT), then no
occurrence of CounterpartyIdentification is allowed.
If CounterpartyType is not present, then any occurrence of CounterpartyIdentification is optional.
On Condition
    /CounterpartyType is present
 And    /CounterpartyType is equal to value 'Multilateral'
Following Must be True
    /CounterpartyIdentification[1] Must be absent
• CounterpartyIdentification2Rule
If at least one occurrence of CounterpartyType is present and is equal to Bilateral (BILA), then at
least one occurrence of CounterpartyIdentification must be present.
If CounterpartyType is not present, then any occurrence of CounterpartyIdentification is optional.
On Condition
    /CounterpartyType is present
 And    /CounterpartyType is equal to value 'Bilateral'
Following Must be True
    /CounterpartyIdentification[1] Must be present
2.4.2.2.2.1  Type <Tp>
Presence: [0..*]
Definition: Specifies the nature of a balance.
Type <Tp> contains one of the following BalanceType11Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 15
Or}   Proprietary <Prtry> [1..1] Text 15
2.4.2.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the nature of a balance, in a coded form.
Datatype: "ExternalSystemBalanceType1Code" on page 65
2.4.2.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the nature of a balance, in a proprietary form.
Datatype: "Max35Text" on page 69
2.4.2.2.2.2  CounterpartyType <CtrPtyTp>
Presence: [1..1]
Definition: Specifies the type of counterparty for which the balance is calculated.
Datatype: "BalanceCounterparty1Code" on page 63
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
15 March 2024
```

