---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.3 SubBalanceType11Choice", "35.1.4.3.2 Proprietary <Prtry>"]
file_pages: [1413]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.3.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1413 to 1413.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1413

```text
CodeName Name Definition
PECA PendingCorporateActionReceipt Balance of financial instrument pending
receipt following a corporate action.
PEDA PendingCorporateActionDelivery Balance of financial instrument pending
delivery following a corporate action.
PEND PendingDelivery Processing has not been completed.
PENR PendingReceipt The instruction is pending receipt of
securities, for example, from a purchase,
loan etc.
PLED Pledged Balance of securities that belong to and
is kept in the safekeeping account
indicated within this message, and that
are pledged.
REGO OutForRegistration Balance of financial instruments
currently being processed by the
institution responsible for registering the
new beneficial owner (or nominee).
RSTR Restricted Balance of financial instruments that
may only be sold under certain
conditions or require legal documents.
OTHR Unclassified Other. See Narrative.
TRAN InTransshipment Transaction has been generated due to
transformation following a corporate
action.
DRAW Drawn Settlement transactions relates to drawn
securities.
WDOC WaitingDocumentation Financial instrument is unavailable due
to missing or incomplete documentation
pertaining to the account, or due to a
missing or incomplete order.
BTRA BeingTransferred Financial instrument is unavailable as a
result of a transfer order, pending
movement in the shareholders' register.
35.1.4.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason a security is not available or additional information about the financial instrument for
which the balance is given, for example, unregistered, registered in nominee name.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1413 March 2026
```

