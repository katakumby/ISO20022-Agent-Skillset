---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.3 ReturnCriteria <RtrCrit>", "2.4.2.2.2.3.1 NameIndicator <NmInd>"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.3.1 NameIndicator <NmInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
ReturnCriteria <RtrCrit> contains the following CashAccountReturnCriteria5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NameIndicator <NmInd> [0..1] Indicator 42
   CurrencyIndicator <CcyInd> [0..1] Indicator 42
   TypeIndicator <TpInd> [0..1] Indicator 43
   MultilateralLimitIndicator <MulLmtInd> [0..1] Indicator 43
   MultilateralBalanceReturnCriteria <MulBalRtrCrit> [0..1]  43
     TypeIndicator <TpInd> [1..1] Indicator 43
     StatusIndicator <StsInd> [1..1] Indicator 43
     ValueDateIndicator <ValDtInd> [1..1] Indicator 44
     ProcessingDateIndicator <PrcgDtInd> [1..1] Indicator 44
     NumberOfPaymentsIndicator <NbOfPmtsInd> [1..1] Indicator 44
   BilateralLimitIndicator <BilLmtInd> [0..1] Indicator 44
   BilateralBalanceReturnCriteria <BilBalRtrCrit> [0..1]  44
     TypeIndicator <TpInd> [1..1] Indicator 45
     StatusIndicator <StsInd> [1..1] Indicator 45
     ValueDateIndicator <ValDtInd> [1..1] Indicator 45
     ProcessingDateIndicator <PrcgDtInd> [1..1] Indicator 45
     NumberOfPaymentsIndicator <NbOfPmtsInd> [1..1] Indicator 46
   StandingOrderIndicator <StgOrdrInd> [0..1] Indicator 46
   AccountOwnerIndicator <AcctOwnrInd> [0..1] Indicator 46
   AccountServicerIndicator <AcctSvcrInd> [0..1] Indicator 46
2.4.2.2.2.3.1  NameIndicator <NmInd>
Presence: [0..1]
Definition: Indicates whether the account name is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
2.4.2.2.2.3.2  CurrencyIndicator <CcyInd>
Presence: [0..1]
Definition: Indicates whether the account currency is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 42 February 2025
```

