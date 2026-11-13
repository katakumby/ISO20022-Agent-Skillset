---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [4, 5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01", "reda.019.001.01", "reda.020.001.01", "reda.021.001.01", "reda.023.001.01", "reda.032.001.01", "reda.035.001.01", "reda.036.001.01", "reda.037.001.01"]
---

# 1 Message Set Overview

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 4 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Securities Account Reference Data message setThis
document describes the Target2-Securities - Securities Reference Data message set. It includes the
new version of the MessageDefinitions that have been developed in the scope of the Target2-Securities
Business Justification (See BJ#042) and approved by the Securities and the Payments Standards
Evaluation Groups under the leadership of the Securities SEG on 02 December 2019.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
reda.018.001.01
SecuritiesAccountCreationRequestV01
The SecuritiesAccountCreationRequest message
message is sent by an instructing party to the
executing party to instruct the creation of a new
securities account with the required account attributes
details.
Usage:
Processing and confirmation of the securities account
creation request message are provided via a
SecuritiesAccountStatusAdvice message.
reda.019.001.01
SecuritiesAccountQueryV01
The SecuritiesAccountQuery message sent by an
instructing party to the executing party to request the
details related to the securities account.
reda.020.001.01
SecuritiesAccountStatusAdviceV01
The SecuritiesAccountStatusAdvice message is send
by the the executing party to an instructing party to
provide the status of the execution of an creation,
modification or deletion of securities account reference
data.
Usage:
When processing information is negative - a failure
occurred in applying the changes the message
accordingly also delivers information about the reason
why the creation or update could not be processed.
When the processing is succesfully performed, the
message includes the related securities account
identification.
reda.021.001.01
SecuritiesAccountReportV01
The SecuritiesAccountReport message sent by the
executing party to an instructing party to provide the
details of the securities account details as requested in
the query.
reda.023.001.01
SecuritiesAccountModificationRequestV01
The SecuritiesAccountModificationRequest message is
sent by an instructing party to the executing party to
instruct the update of an existing securities account by
amending its existing attributes or by providing
additional attibutes details.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Set Overview
Target2-Securities - Securities Account Reference Data 4 December 2019
```

## File page 5

```text
MessageDefinition Definition
Usage:
Processing and confirmation of the securities account
creation request message are provided via a
SecuritiesAccountStatusAdvice message.
reda.032.001.01
SecuritiesAccountDeletionRequestV01
The SecuritiesAccountDeletionRequest message is
sent by an instructing party to the executing party to
request for the deletion of a securities account from the
securities account reference data defined in the system
of the executing party.
Usage:
It aims at instructing the deletion of an existing
securities account providing securities account
identification.
The result of the deletion is provided through a
SecuritiesAccountStatusAdvice message.
reda.035.001.01
SecuritiesAccountActivityAdviceV01
The SecuritieAccountActivityReport message is sent
by the executing party to an instructing party containing
information about changes on securities account
reference data.
Scope and usage:
It aims at informing about the changes occurred during
a business date for securities account reference data.
reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
The SecuritiesAccountAuditTrailQuery message is sent
by an instructing party to the executing party to query
for the securities account audit trail recorded in the
system.
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
The SecuritiesAccountAuditTrailReport message is
sent by the executing party to an instructing party to
provide detailed information on the requested
securities account audit trail recorded in the system.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Set Overview
Target2-Securities - Securities Account Reference Data 5 December 2019
```

