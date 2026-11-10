---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [3, 4, 5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.045.001.01", "reda.046.001.01", "reda.047.001.01", "reda.049.001.01", "reda.050.001.01", "reda.051.001.01"]
---

# 1 Message Set Overview

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 3 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Link Reference Data message set. It includes the
new Account and Securities CSD linking MessageDefinitions that have been developed in the scope of
the Target2-Securities Business Justification (See BJ#042) and approved by the Securities on 21
November 2024.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
reda.045.001.01
SecurityCSDLinkCreationRequestV01
An instructing party sends a
SecurityCSDLinkCreationRequest message to an
executing/servicing party to request the creation of the
link between a financial instrument and a CSD in their
system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.046.001.01
SecurityCSDLinkMaintenanceRequestV01
An instructing party sends a
SecurityCSDLinkMaintenanceRequest message to an
executing/servicing party to request the maintenance
of the link between a financial instrument and a CSD in
their system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.047.001.01
SecurityCSDLinkStatusAdviceV01
An executing/servicing party sends a
SecurityCSDLinkStatusAdvice message to an
instructing party to report the status of a
Approved by the Securities SEG on 21 November 2024. Message Set Overview
Target2-Securities - Link Reference Data 3 December 2024
```

## File page 4

```text
MessageDefinition Definition
SecurityCSDLink Request message previously sent by
the instructing party.
The SecurityCSDLinkStatusAdvice message may be
sent as a response to the request of the instructing
party or not.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish security CSD Link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
reda.049.001.01
AccountLinkCreationRequestV01
reda.050.001.01
AccountLinkMaintenanceRequestV01
SCOPE:
The AccountLinkMaintenanceRequest message is sent
by the instructing party to the executing/servicing party
to request for the maintenance of an account link in
their system.
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
The request is sent when the instructing party identified
a gap in the account link coverage of the executing/
servicing party. The instructing party needs this
account link to be maintained at the executing /
servicing party to perform its activities.
Initiator: instructing party.
Approved by the Securities SEG on 21 November 2024. Message Set Overview
Target2-Securities - Link Reference Data 4 December 2024
```

## File page 5

```text
MessageDefinition Definition
reda.051.001.01
AccountLinkStatusAdviceV01
SCOPE:
The AccountLinkStatusAdvice message is sent by the
executing/servicing party to the instructing party to
provide details about the processing of a request on
account link reference data (create or update).
The instructing party - executing/servicing party
relationship may be:
- Central Securities Depositories (CSD) who would like
to publish account link static data, or
- a Corporate, or
- a Bank, or
- a Market Infrastructure, or
- a Market Data Provider.
USAGE:
Initiator: executing/servicing party
When processing information is negative - a failure
occurred in applying the changes the message
accordingly also delivers information about the reason
why the creation or update could not be processed.
When the processing is successfully performed, the
message includes the related account link
identification.
Approved by the Securities SEG on 21 November 2024. Message Set Overview
Target2-Securities - Link Reference Data 5 December 2024
```

