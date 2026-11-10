---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.15 Person Identification", "12.1.15.1 ContactIdentification2", "12.1.15.1.1 NamePrefix <NmPrfx>"]
file_pages: [459]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.15.1.1 NamePrefix <NmPrfx>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 459 to 459.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 459

```text
12.1.15.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: NamePrefix1Code on page 479
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MIST Mister Title of the person is Mister or Mr.
MISS Miss Title of the person is Miss.
MADM Madam Title of the person is Madam.
12.1.15.1.2  GivenName <GvnNm>
Presence: [0..1]
Definition: First name of a person.
Datatype: Max35Text on page 493
12.1.15.1.3  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: Max35Text on page 493
12.1.15.1.4  PhoneNumber <PhneNb>
Presence: [0..1]
Definition: Collection of information that identifies a phone number, as defined by telecom services.
Datatype: PhoneNumber on page 494
12.1.15.1.5  MobileNumber <MobNb>
Presence: [0..1]
Definition: Collection of information that identifies a mobile phone number, as defined by telecom
services.
Datatype: PhoneNumber on page 494
12.1.15.1.6  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Collection of information that identifies a FAX number, as defined by telecom services.
Datatype: PhoneNumber on page 494
12.1.15.1.7  EmailAddress <EmailAdr>
Presence: [0..1]
Definition: Address for electronic mail (e-mail).
Datatype: Max256Text on page 492
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 459
```

