---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.24 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "4.4.3.27.24.38 UnderlyingAllocation <UndrlygAllcn>"]
file_pages: [558]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.24.38 UnderlyingAllocation <UndrlygAllcn>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 558 to 558.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 558

```text
RemittanceInformation <RmtInf> contains the following elements (see "RemittanceInformation2" on
page 1192 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unstructured <Ustrd> [0..*] Text 1192
4.4.3.27.24.38  UnderlyingAllocation <UndrlygAllcn>
Presence: [0..*]
Definition: Provides information on the underlying allocations that make up the payment.
Usage: Only used by the Securities industry.
Impacted by: C80 "UnderlyingAllocationGuideline"
UnderlyingAllocation <UndrlygAllcn> contains the following TransactionAllocation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C12 558
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 559
   Account <Acct> [1..1] ± C22,
C21
559
   Purpose <Purp> [1..1] ± 559
   Reference <Ref> [1..1] Text 560
   RelatedReferences <RltdRefs> [0..*] ± 560
Constraints
• UnderlyingAllocationGuideline
UnderlyingAllocation may only be present if bilaterally agreed.
4.4.3.27.24.38.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money in the allocation.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
558 March 2026
```

