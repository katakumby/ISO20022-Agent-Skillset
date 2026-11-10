---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2 Balance <Bal>", "2.4.2.2.2.1 Type <Tp>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.2.1 Type <Tp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

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
{Or   Code <Cd> [1..1] CodeSet 45
Or}   Proprietary <Prtry> [1..1] Text 45
2.4.2.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the nature of a balance, in a coded form.
Datatype: "ExternalSystemBalanceType1Code" on page 3245
2.4.2.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the nature of a balance, in a proprietary form.
Datatype: "Max35Text" on page 3328
2.4.2.2.2.2  CounterpartyType <CtrPtyTp>
Presence: [1..1]
Definition: Specifies the type of counterparty for which the balance is calculated.
Datatype: "BalanceCounterparty1Code" on page 3215
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 45 August 2026
```

