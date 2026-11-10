---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.6.24 OwnAccountTransferIndicator <OwnAcctTrfInd>"]
file_pages: [572]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.6.24 OwnAccountTransferIndicator <OwnAcctTrfInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 572 to 572.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 572

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
26.4.6.24  OwnAccountTransferIndicator <OwnAcctTrfInd>
Presence: [0..1]
Definition: Indicates whether the transfer results in a change of beneficial owner.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
26.4.6.25  NonStandardSettlementInformation <NonStdSttlmInf>
Presence: [0..1]
Definition: Additional specific settlement information for non-regulated traded funds.
Datatype: "Max350Text" on page 5403
26.4.6.26  TransferExpensesPaymentType <TrfExpnssPmtTp>
Presence: [0..1]
Definition: Specifies how the payment of fees and taxes as a result of the transfer is covered, that is,
whether by cash or the redemption of units.
TransferExpensesPaymentType <TrfExpnssPmtTp> contains one of the following elements (see
"ChargePaymentMethod1Choice" on page 4453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4453
Or}   Proprietary <Prtry> [1..1] ± 4453
26.4.7 AccountDetails <AcctDtls>
Presence: [1..1]
Definition: Information related to the account from which the financial instrument was withdrawn.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 572 May 2026
```

