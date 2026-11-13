---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.9 RegistrationProcessingStatus <RegnPrcgSts>"]
file_pages: [1913]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.9 RegistrationProcessingStatus <RegnPrcgSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1913 to 1913.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1913

```text
MatchingStatus <MtchgSts> contains one of the following elements (see "MatchingStatus27Choice"
on page 1924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1924
Or}   Proprietary <Prtry> [1..1] ± 1925
35.1.29.22.9  RegistrationProcessingStatus <RegnPrcgSts>
Presence: [1..1]
Definition: Provides the status of the registration processing.
RegistrationProcessingStatus <RegnPrcgSts> contains one of the following
RegistrationProcessingStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1913
Or}   Proprietary <Prtry> [1..1] ± 1913
35.1.29.22.9.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of the registration processing.
Datatype: "RegistrationProcessingStatus1Code" on page 2114
CodeName Name Definition
PACK AcknowledgedAccepted Registration has been acknowledged/
accepted by the issuer/registrar.
REJT Rejected Registration has been rejected by the
issuer/registrar.
35.1.29.22.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of the registration processing.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.22.10  ResponseStatus <RspnSts>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1913 March 2026
```

