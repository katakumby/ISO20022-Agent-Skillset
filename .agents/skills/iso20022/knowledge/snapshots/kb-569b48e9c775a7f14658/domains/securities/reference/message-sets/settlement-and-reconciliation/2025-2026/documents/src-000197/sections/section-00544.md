---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "25.4 Message Building Blocks", "25.4.6 ProcessingStatus <PrcgSts>", "25.4.6.6 Proprietary <Prtry>"]
file_pages: [814]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25.4.6.6 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 814 to 814.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 814

```text
Definition: Modification is pending. It is not known at this time whether modification can be affected.
Pending <Pdg> contains one of the following elements (see "PendingStatus83Choice" on page 2015
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2016
Or}   Reason <Rsn> [1..*]  2016
     Code <Cd> [1..1] ± 2016
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2016
25.4.6.6  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 1877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
25.4.7 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C10 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 814 March 2026
```

