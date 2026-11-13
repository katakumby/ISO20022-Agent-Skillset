---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09", "21.4 Message Building Blocks", "21.4.5 SupplementaryData <SplmtryData>"]
file_pages: [726]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.027.001.09"]
---

# 21.4.5 SupplementaryData <SplmtryData>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 726 to 726.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 726

```text
Definition: Party, either an individual or organisation, whose assets are being invested.
Investor <Invstr> contains the following elements (see "PartyIdentification149" on page 1687 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1687
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1687
Or     ProprietaryIdentification <PrtryId> [1..1] ± 1687
Or     NameAndAddress <NmAndAdr> [1..1] ± 1688
Or}     Country <Ctry> [1..1] CodeSet C7 1688
   LEI <LEI> [0..1] IdentifierSet 1688
21.4.5 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C26 "SupplementaryDataRule"
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
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 726 March 2026
```

