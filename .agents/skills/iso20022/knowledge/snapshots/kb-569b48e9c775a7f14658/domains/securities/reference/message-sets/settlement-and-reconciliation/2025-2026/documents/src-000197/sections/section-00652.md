---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.6 RepoCallRequestStatus <RepoCallReqSts>", "28.4.7.17 DigitalPaymentSettlement <DgtlPmtSttlm>", "28.4.7.17.3 CashSettlementSystemPlace <CshSttlmSysPlc>", "28.4.7.17.3.3 LEI <LEI>"]
file_pages: [982]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.7.17.3.3 LEI <LEI>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 982 to 982.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 982

```text
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C6 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 2185
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
28.4.7.17.3.3  LEI <LEI>
Presence: [1..1]
Definition: Legal entity identification as an alternate identification for a place of safekeeping.
Datatype: "LEIIdentifier" on page 2187
28.4.7.18  OpeningSettlementDate <OpngSttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
OpeningSettlementDate <OpngSttlmDt> contains one of the following elements (see
"SettlementDate19Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1441
Or}   DateCode <DtCd> [1..1] ± 1441
28.4.7.19  TerminationDate <TermntnDt>
Presence: [0..1]
Definition: Closing date/time or maturity date/time of the transaction.
TerminationDate <TermntnDt> contains one of the following elements (see "TerminationDate6Choice"
on page 1436 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1437
Or}   Code <Cd> [1..1]  1437
{Or     Code <Cd> [1..1] CodeSet 1437
Or}     Proprietary <Prtry> [1..1] ± 1437
28.4.7.20  TradeDate <TradDt>
Presence: [0..1]
Definition: Specifies the date/time on which the trade was executed.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 982 March 2026
```

