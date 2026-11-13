---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "25.4 Message Building Blocks", "25.4.5 RequestDetails <ReqDtls>"]
file_pages: [807]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25.4.5 RequestDetails <ReqDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 807 to 807.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 807

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
25.4.5 RequestDetails <ReqDtls>
Presence: [0..1]
Definition: Details of the request.
Impacted by: C3 "ModificationRequestPresenceRule", C4 "OtherProcessingRule", C8
"SettlementConditionModificationApplicabilityRule"
RequestDetails <ReqDtls> contains the following RequestDetails31 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] ± C5 808
   RestrictionReference <RstrctnRef> [0..*] ± 808
   AutomaticBorrowing <AutomtcBrrwg> [0..1] ± 809
   RetainIndicator <RtnInd> [0..1] Indicator 809
   Linkage <Lkg> [0..1] ± 809
   Priority <Prty> [0..1] ± 809
   OtherProcessing <OthrPrcg> [0..*] ± 810
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 810
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 810
   HoldIndicator <HldInd> [0..1] ± 811
   MatchingDenial <MtchgDnl> [0..1] ± 811
   UnilateralSplit <UnltrlSplt> [0..1] ± 811
   Linkages <Lnkgs> [0..*] ± 811
Constraints
• ModificationRequestPresenceRule
At least one securities settlement conditions modification request type must be present.
• OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and receiver.
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 807 March 2026
```

