---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["17 camt.018.001.05 GetBusinessDayInformationV05", "17.4 Message Building Blocks", "17.4.2 BusinessDayInformationQueryDefinition <BizDayInfQryDef>", "17.4.2.2 Criteria <Crit>", "17.4.2.2.2 NewCriteria <NewCrit>", "17.4.2.2.2.2 SearchCriteria <SchCrit>"]
file_pages: [529]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.018.001.05"]
---

# 17.4.2.2.2.2 SearchCriteria <SchCrit>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 529 to 529.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 529

```text
17.4.2.2.2.2  SearchCriteria <SchCrit>
Presence: [0..*]
Definition: Defines the criteria on which the information is extracted.
SearchCriteria <SchCrit> contains the following BusinessDaySearchCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemDate <SysDt> [0..1] Date 529
   SystemIdentification <SysId> [0..*] ± 529
   SystemCurrency <SysCcy> [0..*] CodeSet C1 529
   EventType <EvtTp> [0..1]  530
{Or     Code <Cd> [1..1] CodeSet 530
Or}     Proprietary <Prtry> [1..1] ± 531
   ClosurePeriod <ClsrPrd> [0..1]  531
{Or     FromDateTime <FrDtTm> [1..1] DateTime 532
Or     ToDateTime <ToDtTm> [1..1] DateTime 532
Or}     DateTimeRange <DtTmRg> [1..1] ± 532
17.4.2.2.2.2.1  SystemDate <SysDt>
Presence: [0..1]
Definition: Date for which the availability information is provided.
Datatype: "ISODate" on page 883
17.4.2.2.2.2.2  SystemIdentification <SysId>
Presence: [0..*]
Definition: Unique and unambiguous identification of the system, as assigned by the system
administrator.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
17.4.2.2.2.2.3  SystemCurrency <SysCcy>
Presence: [0..*]
Definition: Currency which may be processed by the system. A system may process transactions in a
single currency or in multiple currencies.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 849
Approved by the Payments SEG on 04 February 2025 camt.018.001.05 GetBusinessDayInformationV05
Cash Management - Maintenance 2024 - 2025 529 February 2025
```

