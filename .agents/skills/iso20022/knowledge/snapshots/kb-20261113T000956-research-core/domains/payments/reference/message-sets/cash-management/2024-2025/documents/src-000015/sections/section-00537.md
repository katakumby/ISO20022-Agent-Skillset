---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks", "30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>", "30.4.2.2 StandingOrderCriteria <StgOrdrCrit>", "30.4.2.2.2 NewCriteria <NewCrit>", "30.4.2.2.2.3 ReturnCriteria <RtrCrit>", "30.4.2.2.2.3.1 StandingOrderIdentificationIndicator <StgOrdrIdInd>"]
file_pages: [702]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4.2.2.2.3.1 StandingOrderIdentificationIndicator <StgOrdrIdInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 702 to 702.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 702

```text
ReturnCriteria <RtrCrit> contains the following StandingOrderReturnCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StandingOrderIdentificationIndicator <StgOrdrIdInd> [0..1] Indicator 702
   TypeIndicator <TpInd> [0..1] Indicator 702
   SystemMemberIndicator <SysMmbInd> [0..1] Indicator 702
   ResponsiblePartyIndicator <RspnsblPtyInd> [0..1] Indicator 703
   CurrencyIndicator <CcyInd> [0..1] Indicator 703
   DebtorAccountIndicator <DbtrAcctInd> [0..1] Indicator 703
   CreditorAccountIndicator <CdtrAcctInd> [0..1] Indicator 703
   AssociatedPoolAccount <AssoctdPoolAcct> [0..1] Indicator 703
   FrequencyIndicator <FrqcyInd> [0..1] Indicator 704
   ExecutionTypeIndicator <ExctnTpInd> [0..1] Indicator 704
   ValidityFromIndicator <VldtyFrInd> [0..1] Indicator 704
   ValidToIndicator <VldToInd> [0..1] Indicator 704
   LinkSetIdentificationIndicator <LkSetIdInd> [0..1] Indicator 704
   LinkSetOrderIdentificationIndicator <LkSetOrdrIdInd> [0..1] Indicator 704
   LinkSetOrderSequenceIndicator <LkSetOrdrSeqInd> [0..1] Indicator 705
   TotalAmountIndicator <TtlAmtInd> [0..1] Indicator 705
   ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 705
30.4.2.2.2.3.1  StandingOrderIdentificationIndicator <StgOrdrIdInd>
Presence: [0..1]
Definition: Defines the criteria used to report on a multilateral balance.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.2  TypeIndicator <TpInd>
Presence: [0..1]
Definition: Indicates whether the standing order type is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
30.4.2.2.2.3.3  SystemMemberIndicator <SysMmbInd>
Presence: [0..1]
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 702 February 2025
```

