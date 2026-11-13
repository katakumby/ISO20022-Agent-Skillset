---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.97 CorporateActionEventType110Choice", "35.1.16.97.2 Proprietary <Prtry>"]
file_pages: [1658]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.97.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1658 to 1658.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1658

```text
CodeName Name Definition
MTNG SecuritiesHoldersMeeting Ordinary or annual or extraordinary or
special general meeting.
INFO Information Information provided by the issuer
having no accounting/financial impact on
the holder.
TNDP TaxOnNonDistributedProceeds Taxable component on non-distributed
proceeds, for example, Australian
deemed income or US 871m income
regulation.
RCLA Reclassification Securities related event which
reclassifies the distribution in various
types of income for US tax withholding
purposes.
35.1.16.97.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Corporate action event type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.98  SettlementOrCorporateActionEvent35Choice
Definition: Choice between transaction type, corporate action event and settlement transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1658
Or}   CorporateActionEventType <CorpActnEvtTp> [1..1] ± C13 1659
35.1.16.98.1  SecuritiesTransactionType <SctiesTxTp>
Presence: [1..1]
Definition: Identifies the type of securities transaction.
SecuritiesTransactionType <SctiesTxTp> contains one of the following elements (see
"SecuritiesTransactionType48Choice" on page 1565 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1565
Or}   Proprietary <Prtry> [1..1] ± 1568
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1658 March 2026
```

