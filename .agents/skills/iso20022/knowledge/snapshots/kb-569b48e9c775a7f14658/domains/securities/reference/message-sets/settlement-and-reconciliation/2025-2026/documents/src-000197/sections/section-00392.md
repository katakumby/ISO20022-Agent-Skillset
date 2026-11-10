---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.4 Message Building Blocks", "18.4.4 InferredMatchingStatus <IfrrdMtchgSts>", "18.4.7.20 DigitalPaymentSettlement <DgtlPmtSttlm>", "18.4.7.20.3 CashSettlementSystemPlace <CshSttlmSysPlc>", "18.4.7.20.3.3 LEI <LEI>"]
file_pages: [591]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.4.7.20.3.3 LEI <LEI>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 591 to 591.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 591

```text
Datatype: "AnyBICDec2014Identifier" on page 2185
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
18.4.7.20.3.3  LEI <LEI>
Presence: [1..1]
Definition: Legal entity identification as an alternate identification for a place of safekeeping.
Datatype: "LEIIdentifier" on page 2187
18.4.7.21  LateDeliveryDate <LateDlvryDt>
Presence: [0..1]
Definition: Date and time after the settlement date specified in the trade, used for pool trades resulting
from the original To Be Assigned (TBA) securities.
LateDeliveryDate <LateDlvryDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
18.4.7.22  ExpectedSettlementDate <XpctdSttlmDt>
Presence: [0..1]
Definition: Date/time at which the sender expects settlement.
ExpectedSettlementDate <XpctdSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
18.4.7.23  ExpectedValueDate <XpctdValDt>
Presence: [0..1]
Definition: For against payment transactions, the value date/time at which the sender expects the
settlement amount to be credited or debited.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 591 March 2026
```

