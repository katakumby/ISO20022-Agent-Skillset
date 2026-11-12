---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["18 semt.002.001.02 CustodyStatementOfHoldingsV02", "18.4 Message Building Blocks", "18.4.4 MessagePagination <MsgPgntn>"]
file_pages: [380]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.02"]
---

# 18.4.4 MessagePagination <MsgPgntn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 380 to 380.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 380

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference2" on
page 4538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4538
   ReferenceIssuer <RefIssr> [0..1] ± 4538
   MessageName <MsgNm> [0..1] Text 4538
18.4.4 MessagePagination <MsgPgntn>
Presence: [1..1]
Definition: Pagination of the message.
MessagePagination <MsgPgntn> contains the following elements (see "Pagination" on page 4833 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4833
   LastPageIndicator <LastPgInd> [1..1] Indicator 4833
18.4.5 StatementGeneralDetails <StmtGnlDtls>
Presence: [1..1]
Definition: General information related to the custody statement of holdings.
StatementGeneralDetails <StmtGnlDtls> contains the following Statement7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 380
   StatementDateTime <StmtDtTm> [1..1] ± 381
   CreationDateTime <CreDtTm> [0..1] ± 381
   Frequency <Frqcy> [1..1] ± 381
   UpdateType <UpdTp> [1..1] ± 381
   ActivityIndicator <ActvtyInd> [1..1] Indicator 382
   StatementBasis <StmtBsis> [1..1] ± 382
   ReportNumber <RptNb> [0..1] Text 382
18.4.5.1  Reference <Ref>
Presence: [1..1]
Definition: Reference of the statement.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 semt.002.001.02 CustodyStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 380 May 2026
```

