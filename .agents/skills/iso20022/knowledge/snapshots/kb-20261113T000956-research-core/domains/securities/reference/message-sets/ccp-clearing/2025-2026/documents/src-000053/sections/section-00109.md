---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.9 NonClearingMember <NonClrMmb>"]
file_pages: [148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.9 NonClearingMember <NonClrMmb>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 148 to 148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 148

```text
4.4.5.4.9  NonClearingMember <NonClrMmb>
Presence: [0..1]
Definition: Provides details about the non clearing member identification and account.
NonClearingMember <NonClrMmb> contains the following elements (see
PartyIdentificationAndAccount227 on page 457 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 457
   AlternateIdentification <AltrnId> [0..1] ± 457
   AdditionalInformation <AddtlInf> [0..1] ± C3 457
   ClearingAccount <ClrAcct> [0..1] ± 458
4.4.5.4.10  TradeDate <TradDt>
Presence: [1..1]
Definition: Provides the date or date and time of trade transaction.
TradeDate <TradDt> contains one of the following elements (see DateAndDateTime2Choice on
page 390 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
4.4.5.4.11  TransactionDateAndTime <TxDtAndTm>
Presence: [0..1]
Definition: Date and time used to determine the price applicable to a trade. If the trade is registered
"after market" hours, the trading price will the price of the day but the actual trade date will be the next
working day.
Datatype: ISODateTime on page 487
4.4.5.4.12  SettlementDate <SttlmDt>
Presence: [0..1]
Definition: Provides the contractual settlement date.
SettlementDate <SttlmDt> contains one of the following DateFormat66Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 149
Or}   DateCode <DtCd> [1..1]  149
{Or     Code <Cd> [1..1] CodeSet 149
Or}     Proprietary <Prtry> [1..1] ± 149
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 148
```

