---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.2 Message Datatypes", "12.2.2 CodeSet", "12.2.2.12 DeliveryReceiptType2Code"]
file_pages: [477]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.2.2.12 DeliveryReceiptType2Code

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 477 to 477.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 477

```text
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
12.2.2.12  DeliveryReceiptType2Code
Definition: Specifies how the transaction is to be settled.
Type: CodeSet
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
12.2.2.13  EventFrequency6Code
Definition: Specifies the regularity of an event.
Type: CodeSet
CodeName Name Definition
DAIL Daily Event takes place every day.
INDA IntraDay Event takes place several times a day.
ONDE OnDemand Event takes place on demand.
12.2.2.14  ExternalAccountIdentification1Code
Definition: Specifies the external account identification scheme name code in the format of character
string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Format
minLength 1
maxLength 4
12.2.2.15  ExternalFinancialInstrumentIdentificationType1Code
Definition: Specifies the external financial instrument identification type scheme name code in the
format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 477
```

