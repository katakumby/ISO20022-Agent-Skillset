---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.3 UserIdentification <UsrId>"]
file_pages: [441]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.3 UserIdentification <UsrId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 441 to 441.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 441

```text
SendingOrganisationIdentification <SndgOrgId> contains the following elements (see
"OrganisationIdentification31" on page 1659 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C5 1659
   Other <Othr> [0..*]  1660
     Identification <Id> [1..1] Text 1660
     SchemeName <SchmeNm> [0..1]  1660
{Or       Code <Cd> [1..1] CodeSet 1660
Or}       Proprietary <Prtry> [1..1] Text 1661
     Issuer <Issr> [0..1] Text 1661
13.4.7.3  UserIdentification <UsrId>
Presence: [0..1]
Definition: Unique and unambiguous way to identify the user that created the message instance.
Datatype: "Max35Text" on page 2192
13.4.7.4  ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Provides details on the processing status of the transaction.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 441 March 2026
```

