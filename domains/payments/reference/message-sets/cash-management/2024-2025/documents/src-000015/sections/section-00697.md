---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.3 Date"]
file_pages: [883]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.3 Date

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 883 to 883.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 883

```text
CodeName Name Definition
IEXE IncorrectBuyerOrSeller Instruction indicates an incorrect buyer
(receiver) or seller (deliverer).
NCRR DisagreementCurrencySettlementAmount Counterparty disagrees with the
currency of the settlement amount.
NMAS NoMatchingStarted Matching process has not yet started.
SAFE DisagreementSafekeepingAccount Safekeeping account used as a
matching criteria on the market
concerned does not match.
DTRD DisagreementTradeDate Counterparty disagrees with the trade
date.
LATE YourInstructionTooLateForMatching Instruction received too late for
matching.
TERM DisagreementClosingDateTime Closing date/time does not match.
ICUS DisagreementReceivingOrDeliveringCustodian Incorrect delivering or receiving
custodian.
37.2.3 Date
37.2.3.1  ISODate
Definition: A particular point in the progression of time in a calendar year expressed in the YYYY-MM-
DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C
Recommendation 28 October 2004" which is aligned with ISO 8601.
Type: Date
37.2.4 DateTime
37.2.4.1  ISODateTime
Definition: A particular point in the progression of time defined by a mandatory date and a mandatory
time component, expressed in either UTC time format (YYYY-MM-DDThh:mm:ss.sssZ), local time with
UTC offset format (YYYY-MM-DDThh:mm:ss.sss+/-hh:mm), or local time format (YYYY-MM-
DDThh:mm:ss.sss). These representations are defined in "XML Schema Part 2: Datatypes Second
Edition - W3C Recommendation 28 October 2004" which is aligned with ISO 8601.
Note on the time format:
1) beginning / end of calendar day
00:00:00 = the beginning of a calendar day
24:00:00 = the end of a calendar day
2) fractions of second in time format
Decimal fractions of seconds may be included. In this case, the involved parties shall agree on the
maximum number of digits that are allowed.
Type: DateTime
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 883 February 2025
```

