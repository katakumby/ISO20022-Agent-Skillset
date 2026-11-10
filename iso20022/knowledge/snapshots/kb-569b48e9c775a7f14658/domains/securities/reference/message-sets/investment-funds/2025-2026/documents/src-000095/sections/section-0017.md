---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"]
content_origin: "source-transcription"
---

# Portfolio Transfer Management

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Groups / Portfolio Transfer Management.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P144** Portfolio Transfer Management

**P145** Portfolio discovery messages are used to request and provide information about financial instruments held on behalf of the client.

[T10 - complete table](../tables/tbl-0010.md)

**P146** Portfolio transfer messages are used to instruct the transfer of one or more assets from an investor's account at an old plan manager (transferor) to an account with the new plan manager (transferee). 

[T11 - complete table](../tables/tbl-0011.md)

**P147** Transfer messages are used to instruct the transfer of a given amount/quantity of a specified financial instrument from one account to another own account or to a third party account. Specific messages have been created for transfer out and transfer in.

[T12 - complete table](../tables/tbl-0012.md)

**P148** The transfer status reporting messages allow a party to report on the status of transfer instructions and transfer cancellation instructions, and to request a status report. 

[T13 - complete table](../tables/tbl-0013.md)

**P149** For the portfolio transfer, transfer and transfer status messages, concurrent versions are supported. See the section 2.7 'Concurrent Versions of Transfer Messages'.

