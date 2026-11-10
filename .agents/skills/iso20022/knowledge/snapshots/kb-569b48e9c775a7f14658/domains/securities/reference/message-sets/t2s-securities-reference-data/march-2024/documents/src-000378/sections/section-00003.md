---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [4, 5, 6, 7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01", "reda.007.001.01", "reda.008.001.01", "reda.009.001.01", "reda.010.001.01", "reda.012.001.01", "reda.013.001.01", "reda.029.001.01", "reda.030.001.01", "reda.033.001.01", "reda.034.001.01"]
---

# 1 Message Set Overview

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 4 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Securities Reference Data message set. It includes
the new version of the MessageDefinitions that have been developed in the scope of the Target2-
Securities Business Justification (See BJ#042) and approved by the Securities and the Payments
Standards Evaluation Groups under the leadership of the Securities SEG on 28 June 2021.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
reda.006.001.01
SecurityCreationRequestV01
An instructing party sends a SecurityCreationRequest
message to an executing/servicing party to request the
creation of financial instrument static details in their
system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.007.001.01
SecurityMaintenanceRequestV01
An instructing party sends a
SecurityMaintenanceRequest message to an
executing/servicing party to request the maintenance
of financial instrument details in their system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.008.001.01
SecurityCreationStatusAdviceV01
An executing/servicing party sends a
SecurityCreationStatusAdvice message to an
instructing party to report the status of a
SecurityCreationRequest message previously sent by
the instructing party.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Set Overview
Target2-Securities - Securities Reference Data 4 March 2024
```

## File page 5

```text
MessageDefinition Definition
The SecurityCreationStatusAdvice message may be
sent as a response to the request of the instructing
party or not.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.009.001.01
SecurityActivityAdviceV01
The SecurityActivityReport message is sent by the
executing party to an instructing party containing
information about changes on securities reference
data.
Scope and usage:
It aims at informing about the changes occurred during
a business date for securities reference data.
reda.010.001.01
SecurityQueryV01
An instructing party sends a SecurityQuery message to
an executing/servicing party to request a report of
financial instrument details in their system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.012.001.01
SecurityReportV01
An executing/servicing party sends a SecurityReport
message to an instructing party to advise the last
known image of securities data's.
The report may be sent upon request (for example a
query) of the instructing party or push by the executing/
servicing party.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Set Overview
Target2-Securities - Securities Reference Data 5 March 2024
```

## File page 6

```text
MessageDefinition Definition
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
Initiator: executing/servicing party.
reda.013.001.01
SecurityDeletionRequestV01
An instructing party sends a SecurityDeletionRequest
message to an executing/servicing party to advice the
complete removal of a financial instrument entry from
their system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.029.001.01
SecurityMaintenanceStatusAdviceV01
An executing/servicing party sends a
SecurityMaintenanceStatusAdvice message to an
instructing party to report the status of a
SecurityMaintencanceRequest message previously
sent by the instructing party.
The SecurityMaintenanceStatusAdvice message may
be sent as a response to the request of the instructing
party or not.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.030.001.01
SecurityDeletionStatusAdviceV01
An executing/servicing party sends a
SecurityDeletionStatusAdvice message to an
instructing party to report the status of a
SecurityDeletionRequest message previously sent by
the instructing party.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Set Overview
Target2-Securities - Securities Reference Data 6 March 2024
```

## File page 7

```text
MessageDefinition Definition
The SecurityDeletionStatusAdvice message is sent as
a response to the request of the instructing party.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.033.001.01
SecuritiesAuditTrailQueryV01
The SecuritiesAuditTrailQuery message is sent by an
instructing party to the executing party to query for the
securities audit trail recorded in the system.
reda.034.001.01
SecuritiesAuditTrailReportV01
The SecuritiesAuditTrailReport message is sent by the
executing party to an instructing party to provide
detailed information on the requested securities audit
trail recorded in the system.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Set Overview
Target2-Securities - Securities Reference Data 7 March 2024
```

