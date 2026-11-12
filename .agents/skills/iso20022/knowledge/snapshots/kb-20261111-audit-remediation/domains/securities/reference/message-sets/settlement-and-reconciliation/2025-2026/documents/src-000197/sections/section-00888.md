---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.4 Message Building Blocks", "33.4.7 TransactionDetails <TxDtls>", "33.4.7.11 Investor <Invstr>"]
file_pages: [1321]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.4.7.11 Investor <Invstr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1321 to 1321.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1321

```text
33.4.7.11  Investor <Invstr>
Presence: [0..1]
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
33.4.8 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C25 "SupplementaryDataRule"
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
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1321 March 2026
```

