---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "24.4 Message Building Blocks", "24.4.4 RequestDetails <ReqDtls>", "24.4.4.1 Reference <Ref>"]
file_pages: [790]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.030.001.10"]
---

# 24.4.4.1 Reference <Ref>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 790 to 790.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 790

```text
RequestDetails <ReqDtls> contains the following RequestDetails31 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] ± C13 790
   RestrictionReference <RstrctnRef> [0..*] ± 791
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 791
   RetainIndicator <RtnInd> [0..1] Indicator 792
   Linkage <Lkg> [0..1] ± 792
   Priority <Prty> [0..1] ± 792
   OtherProcessing <OthrPrcg> [0..*] ± 792
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 793
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 793
   HoldIndicator <HldInd> [0..1] ± 793
   MatchingDenial <MtchgDnl> [0..1] ± 794
   UnilateralSplit <UnltrlSplt> [0..1] ± 794
   Linkages <Lnkgs> [0..*] ± 794
Constraints
• ModificationRequestPresenceRule
At least one securities settlement conditions modification request type must be present.
• OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and receiver.
• SettlementConditionModificationApplicabilityRule
All settlement condition modification request types do not apply to all account servicers.
24.4.4.1  Reference <Ref>
Presence: [1..1]
Definition: References of the transaction for which the securities settlement condition modification is
requested.
Impacted by: C13 "ReferencePresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 790 March 2026
```

