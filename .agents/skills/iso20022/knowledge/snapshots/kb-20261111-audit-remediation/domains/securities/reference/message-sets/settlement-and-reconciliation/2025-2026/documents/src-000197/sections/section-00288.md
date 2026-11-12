---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.4 Message Building Blocks", "12.4.6 AdditionalQueryParameters <AddtlQryParams>", "12.4.6.2 Reason <Rsn>", "12.4.6.2.12 PendingModificationReason <PdgModRsn>"]
file_pages: [430, 431, 432]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.4.6.2.12 PendingModificationReason <PdgModRsn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 430 to 432.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 430

```text
12.4.6.2.12  PendingModificationReason <PdgModRsn>
Presence: [0..1]
Definition: Specifies the reason why the modification request is pending.
PendingModificationReason <PdgModRsn> contains one of the following elements (see
"PendingReason28Choice" on page 1904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1905
Or}   Proprietary <Prtry> [1..1] ± 1905
12.4.6.2.13  UnmatchedReason <UmtchdRsn>
Presence: [0..1]
Definition: Specifies the reason why the instruction has an unmatched status.
UnmatchedReason <UmtchdRsn> contains one of the following elements (see
"UnmatchedReason22Choice" on page 2001 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2001
Or}   Proprietary <Prtry> [1..1] ± 2003
12.4.6.3  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..*]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C2 "DescriptionPresenceRule", C3 "DescriptionUsageRule", C4 "ISINGuideline", C5
"ISINPresenceRule", C6 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 1474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1475
   OtherIdentification <OthrId> [0..*]  1475
     Identification <Id> [1..1] Text 1475
     Suffix <Sfx> [0..1] Text 1475
     Type <Tp> [1..1] ± 1476
   Description <Desc> [0..1] Text 1476
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 430 March 2026
```

## File page 431

```text
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
12.4.7 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C15 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 431 March 2026
```

## File page 432

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 432 March 2026
```

