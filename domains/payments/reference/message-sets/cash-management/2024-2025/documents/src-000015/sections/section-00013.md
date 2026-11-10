---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2.2.4 Balance <Bal>", "2.4.2.2.2.2.4.1 Type <Tp>"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.2.4.1 Type <Tp>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

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
2.4.2.2.2.2.4.1  Type <Tp>
Presence: [0..*]
Definition: Specifies the nature of a balance.
Type <Tp> contains one of the following BalanceType11Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 32
Or}   Proprietary <Prtry> [1..1] Text 32
2.4.2.2.2.2.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the nature of a balance, in a coded form.
Datatype: "ExternalSystemBalanceType1Code" on page 856
2.4.2.2.2.2.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the nature of a balance, in a proprietary form.
Datatype: "Max35Text" on page 889
2.4.2.2.2.2.4.2  CounterpartyType <CtrPtyTp>
Presence: [1..1]
Definition: Specifies the type of counterparty for which the balance is calculated.
Datatype: "BalanceCounterparty1Code" on page 850
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 32 February 2025
```

