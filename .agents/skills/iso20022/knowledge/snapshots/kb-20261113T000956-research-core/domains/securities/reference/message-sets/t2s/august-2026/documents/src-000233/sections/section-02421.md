---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.4 ActiveCurrencyCode"]
file_pages: [3212]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.4 ActiveCurrencyCode

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3212 to 3212.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3212

```text
CodeName Name Definition
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
NSTP NotStraightThroughProcessing Instruction was not straight through
processing and had to be processed
manually.
RQWV AcceptedWithoutVotingRights Instruction registration is accepted but
the registration is not in full, that is, not
with voting rights.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
82.2.2.4  ActiveCurrencyCode
Definition: A code allocated to a currency by a Maintenance Agency under an international identification
scheme as described in the latest edition of the international standard ISO 4217 "Codes for the
representation of currencies and funds".
Type: CodeSet
Format
pattern [A-Z]{3,3}
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
82.2.2.5  ActiveOrHistoricCurrencyCode
Definition: A code allocated to a currency by a Maintenance Agency under an international identification
scheme, as described in the latest edition of the international standard ISO 4217 "Codes for the
representation of currencies and funds".
Type: CodeSet
Format
pattern [A-Z]{3,3}
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3212 August 2026
```

