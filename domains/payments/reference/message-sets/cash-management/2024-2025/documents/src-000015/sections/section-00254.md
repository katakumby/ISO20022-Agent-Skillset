---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.4 Message Building Blocks", "8.4.2 LimitQueryDefinition <LmtQryDef>", "8.4.2.2 LimitCriteria <LmtCrit>", "8.4.2.2.2 NewCriteria <NewCrit>", "8.4.2.2.2.2 SearchCriteria <SchCrit>", "8.4.2.2.2.2.1 SystemIdentification <SysId>"]
file_pages: [376]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.4.2.2.2.2.1 SystemIdentification <SysId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 376 to 376.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 376

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or     Date <Dt> [1..1] Date 388
Or     Period <Prd> [1..1] ± 388
Or     FromDate <FrDt> [1..1] Date 388
Or}     ToDate <ToDt> [1..1] Date 388
Constraints
• BilateralLimitCounterparty3Rule
If at least one occurrence of CurrentLimitType is present and is MULT, then no occurrence of
BilateralLimitCounterpartyIdentification is allowed.
If no occurrence of CurrentLimitType is MULT, then any occurrence of
BilateralLimitCounterpartyIdentification is optional.
If CurrentLimitType is not present, then any occurrence of BilateralLimitCounterpartyIdentification is
optional.
On Condition
    /CurrentLimitType[1] is present
 And    /CurrentLimitType[*]/Code is equal to value 'Multilateral'
Following Must be True
    /BilateralLimitCounterpartyIdentification[1] Must be absent
• BilateralLimitCounterparty4Rule
If at least one occurrence of DefaultLimitType is present and is MULT, then no occurrence of
BilateralLimitCounterpartyIdentification is allowed.
If no occurrence of DefaultLimitType is MULT, then any occurrence of
BilateralLimitCounterpartyIdentification is optional.
If DefaultLimitType is not present, then any occurrence of BilateralLimitCounterpartyIdentification is
optional.
On Condition
    /DefaultLimitType[1] is present
 And    /DefaultLimitType[*]/Code is equal to value 'Multilateral'
Following Must be True
    /BilateralLimitCounterpartyIdentification[1] Must be absent
8.4.2.2.2.2.1  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 376 February 2025
```

