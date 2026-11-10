---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [4, 5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.014.001.02", "reda.015.001.01", "reda.016.001.01", "reda.017.001.02", "reda.022.001.02", "reda.031.001.01", "reda.041.001.02", "reda.042.001.01", "reda.043.001.02"]
---

# 1 Message Set Overview

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 4 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
1 Message Set Overview
Introduction
This document describes the Target2-Securities - Party Reference Data message set. It includes the
new version of the MessageDefinitions that have been added as part of the maintenance cycle
2023-2024 (See MCR #234) and approved by the Securities and the Payments Standards Evaluation
Groups under the leadership of the Securities SEG on 15 February 2024.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
reda.014.001.02
PartyCreationRequestV02
Scope:
The PartyCreationRequest message is sent by an
instructing party to the executing party to request for
the creation of party reference data for a new party in
the executing system.
Usage:
It aims at instructing the creation of a new party with
corresponding details.
Processing and confirmation of the party creation
request are provided via a party status advice.
reda.015.001.01
PartyQueryV01
Scope:
The PartyQuery message is sent by a central
securities depository, a national central bank, a central
securities depository participant, a central counter
party, a payment bank, a trading party or a stock
exchange to the executing party to query for the party
reference data of a party defined in the system.
reda.016.001.01
PartyStatusAdviceV01
Scope:
The PartyStatusAdvice message is sent by the
executing party to the instructing party to provide
details about the processing of a request on party
reference data (create or update).
Usage:
When processing information is negative - a failure
occurred in applying the changes the message
accordingly also delivers information about the reason
why the creation or update could not be processed.
When processing is successfully performed, the
message includes the related party identification.
reda.017.001.02
PartyReportV02
Scope:
The PartyReport message is sent by the executing
party to a central securities depository, a national
central bank, a central securities depository participant,
a central counter party, a payment bank, a trading
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Set Overview
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
4 March 2024
```

## File page 5

```text
MessageDefinition Definition
party or a stock exchange to provide detailed
information on the requested party reference data of
the party defined in the system.
reda.022.001.02
PartyModificationRequestV02
Scope:
The PartyModificationRequest message is sent by the
instructing party to the executing party to request for an
update of the party reference data of a party defined in
the executing system.
Usage:
It aims at instructing the update of an existing party by
amending its existing details or by providing additional
details.
Processing and confirmation of the party modification
request message are provided via a party status
advice.
reda.031.001.01
PartyDeletionRequestV01
Scope:
The PartyDeletionRequest message is sent by the
instructing party to the executing party to request a
deletion of a party defined in the executing system.
Usage:
It aims at instructing the deletion of an existing party by
providing its identification.
Processing of the party deletion request message is
provided via a party status advice.
reda.041.001.02
PartyActivityAdviceV02
The PartyActivityReport message is sent by the
executing party to an instructing party containing
information about changes on party reference data.
Scope and usage:
It aims at informing about the changes occurred during
a business date for party reference data.
reda.042.001.01
PartyAuditTrailQueryV01
The PartyAuditTrailQuery message is sent by an
instructing party to the executing party to query for the
party audit trail recorded in the system.
reda.043.001.02
PartyAuditTrailReportV02
The PartyAuditTrailReport message is sent by the
executing party to an instructing party to provide
detailed information on the requested party audit trail
recorded in the system.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Set Overview
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
5 March 2024
```

