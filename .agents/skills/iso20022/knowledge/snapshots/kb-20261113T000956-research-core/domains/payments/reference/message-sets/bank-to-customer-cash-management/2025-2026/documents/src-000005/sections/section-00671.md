---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.2 CodeSet", "6.2.2.58 Priority2Code"]
file_pages: [904]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.2.58 Priority2Code

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 904 to 904.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 904

```text
CodeName Name Definition
PARV Par Price is the face amount.
6.2.2.58  Priority2Code
Definition: Specifies the priority level of an event.
Type: CodeSet
CodeName Name Definition
HIGH High Priority level is high.
NORM Normal Priority level is normal.
6.2.2.59  QueryType3Code
Definition: Specifies the nature of the request, that is whether all information be returned or only
information that has changed since the last similar request was returned.
Type: CodeSet
CodeName Name Definition
ALLL All Specifies that the query requests that all
matching items be returned.
CHNG Changed Specifies that the query requests that
only new matching items since the last
similar query be returned.
MODF Modified Specifies that the query requests that
only items that have changed since the
last query be returned.
6.2.2.60  RemittanceLocationMethod2Code
Definition: Specifies the method used to deliver the remittance advice information.
Type: CodeSet
CodeName Name Definition
FAXI Fax Remittance advice information must be
faxed.
EDIC ElectronicDataInterchange Remittance advice information must be
sent through Electronic Data Interchange
(EDI).
URID UniformResourceIdentifier Remittance advice information needs to
be sent to a Uniform Resource Identifier
(URI). URI is a compact string of
characters that uniquely identify an
abstract or physical resource. URI's are
the super-set of identifiers, such as
URLs, email addresses, ftp sites, etc,
and as such, provide the syntax for all of
the identification schemes.
EMAL EMail Remittance advice information must be
sent through e-mail.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
904 March 2026
```

