---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["8 MX secl.007.001.03 BuyInNotificationV03", "8.4 Message Building Blocks", "8.4.3 NotificationDetails <NtfctnDtls>"]
file_pages: [260]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.007.001.03"]
---

# 8.4.3 NotificationDetails <NtfctnDtls>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 260 to 260.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 260

```text
ClearingMember <ClrMmb> contains one of the following elements (see PartyIdentification35Choice
on page 452 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C4 452
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 452
8.4.3 NotificationDetails <NtfctnDtls>
Presence: [0..1]
Definition: Indicates if the message is a notification or a warning and gives the option to specify the buy
in date.
NotificationDetails <NtfctnDtls> contains the following BuyIn4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   WarningIndicator <WrngInd> [0..1] Indicator 260
   ExpectedBuyInDate <XpctdBuyInDt> [1..1]  260
{Or     Date <Dt> [1..1] Date 261
Or}     DateCode <DtCd> [1..1] ± 261
   CancellationLimitDate <CxlLmtDt> [0..1] Date 261
   BuyInReversionDate <BuyInRvrsnDt> [0..1] Date 261
8.4.3.1  WarningIndicator <WrngInd>
Presence: [0..1]
Definition: Indicates whether the message is a warning only or a notification.
Datatype: One of the following values must be used (see YesNoIndicator on page 490):
• Meaning When True: Yes
• Meaning When False: No
8.4.3.2  ExpectedBuyInDate <XpctdBuyInDt>
Presence: [1..1]
Definition: Provides the date at which the buy-in will occur.
ExpectedBuyInDate <XpctdBuyInDt> contains one of the following DateFormat15Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 261
Or}   DateCode <DtCd> [1..1] ± 261
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 260
```

