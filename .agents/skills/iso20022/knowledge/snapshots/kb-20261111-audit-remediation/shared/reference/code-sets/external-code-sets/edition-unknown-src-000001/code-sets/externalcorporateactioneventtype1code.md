---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalCorporateActionEventType1Code"]
code_set: "ExternalCorporateActionEventType1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalCorporateActionEventType1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalCorporateActionEventType1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the corporate action event type, as published in an external corporate action event type code set.
External code sets can be downloaded from www.iso20022.org.
*`ACTV`-Trading in the security has commenced or security has been re-activated after a suspension in trading.
*`ATTI`-Combination of different security types to create a unit. Units are usually comprised of warrants and bonds or warrants and equities. Securities may be combined at the request of the security holder or based on market convention.
*`BRUP`-Legal status of a company unable to pay creditors. Bankruptcy usually involves a formal court ruling. Securities may become valueless.
*`DFLT`-Failure by the company to perform obligations defined as default events under the bond agreement and that have not been remedied.
*`BONU`-Bonus or capitalisation issue. Security holders receive additional assets free of payment from the issuer, in proportion to their holding.
*`EXRI`-Call or exercise on nil paid securities or intermediate securities resulting from an intermediate securities distribution (RHDI). This code is used for the second event, when an intermediate securities' issue (rights/coupons) is composed of two events, the first event being the distribution of intermediate securities.
*`CAPD`-Corporate event pays shareholders an amount in cash issued from the capital account. There is no reduction to the face value of a single share (or the share has no par value). The number of circulating shares remains unchanged.
*`CAPG`-Event is the distribution of profits resulting from the sale of securities. Shareholders of mutual funds, unit trusts, or SICAVs are recipients of capital gains distributions and are often reinvested in additional shares of the fund.
*`CAPI`-Increase of the current principal of a debt instrument without increasing the nominal value. It normally arises from the incorporation of due but unpaid interest into the principal. This is commonly done by increasing the pool factor value, for example, capitalisation, and negative amortisation.
*`DRCA`-Distribution to shareholders of cash resulting from the selling of non-eligible securities, for example, in the frame of a depositary receipt program.
*`DVCA`-Distribution of cash to shareholders, in proportion to their equity holding. Ordinary dividends are recurring and regular. Shareholder must take cash and may be offered a choice of currency.
*`CHAN`-Information regarding a change further described in the corporate action details.
*`COOP`-Company option may be granted by the company, allowing the holder to take up shares at some future date(s) at a pre arranged price in the company. A company may not grant options which enable the holder to take up unissued shares at a time which is five or more years from the date of the grant. Option holders are not members of a company. They are contingent creditors of a company and hence may, in some instances, be entitled to vote on and be bound by a scheme of arrangement between the creditors and the company. As many options have multiple exercise periods a company option will either lapse or carry on to the next expiry date.
*`CLSA`-Situation where interested parties seek restitution for financial loss. The security holder may be offered the opportunity to join a class action proceeding and would need to respond with an instruction.
*`CONS`-Procedure that aims to obtain consent of holder to a proposal by the issuer or a third party without convening a meeting. For example, consent to change the terms of a bond.
*`CONV`-Conversion of securities (generally convertible bonds or preferred shares) into another form of securities (usually common shares) at a pre-stated price/ratio.
*`CREV`-Occurrence of credit derivative for which the issuer of one or several underlying securities is unable to fulfill its financial obligations (as defined in terms and conditions).
*`DECR`-Reduction of face value of a single share or the value of fund assets. The number of circulating shares/units remains unchanged. This event may include a cash payout to holders.
*`DETI`-Separation of components that comprise a security, for example, usually units comprised of warrants and bond or warrants and equity. Units may be broken up at the request of the security holder or based on market convention.
*`DSCL`-Requirement for holders or beneficial owners to disclose their name, location and holdings of any issue to the issuer.
*`DVOP`-Distribution of a dividend to shareholders with a choice of benefit to receive. Shareholders may choose to receive shares or cash. To be distinguished from DRIP as the company creates new share capital in exchange for the dividend rather than investing the dividend in the market.
*`DRIP`-Dividend payment where holders can keep cash or have the cash reinvested in the market by the issuer into additional shares in the issuing company. To be distinguished from DVOP as the company invests the dividend in the market rather than creating new share capital in exchange for the dividend.
*`DRAW`-Securities are redeemed in part before the scheduled final maturity date. It is done without any pool factor reduction. The redemption is reflected in a debit of the face amount (FAMT). Drawing is distinct from partial call since drawn bonds are chosen by lottery. Therefore, not every holder is affected in the same way.
*`DTCH`-Action by a party wishing to acquire a security. Holders of the security are invited to make an offer to sell, within a specific price range. The acquiring party will buy from the holder with lowest offer.
*`EXOF`-Exchange of holdings for other securities and/or cash. The exchange can be either mandatory or voluntary involving the exchange of outstanding securities for different securities and/or cash. For example "exchange offer", "capital reorganisation" or "funds separation".
*`REDM`-Redemption of an entire issue outstanding of securities, for example, bonds, preferred equity, funds, by the issuer or its agent, for example, asset manager, at final maturity.
*`MCAL`-Redemption of an entire issue outstanding of securities, for example, bonds, preferred equity, funds, by the issuer or its agent, for example, asset manager, before final maturity.
*`INCR`-Increase in the face value of a single security. The number of circulating securities remains unchanged.
*`PPMT`-Instalment towards the purchase of equity capital, subject to an agreement between an issuer and a purchaser.
*`INTR`-Interest payment distributed to holders of an interest bearing asset.
*`RHDI`-Distribution of intermediate securities that gives the holder the right to take part in a future event.
*`LIQU`-Distribution of cash, assets or both. Debt may be paid in order of priority based on preferred claims to assets specified by the security.
*`EXTM`-As stipulated in the security's Terms and Conditions, the issuer or the holder may prolong the maturity date of a security. After extension, the security details may differ from the original issue. An issuer initiated extension may be subject to holder's approval.
*`MRGR`-Exchange of outstanding securities, initiated by the issuer which may include options, as the result of two or more companies combining assets, that is, an external, third party company. Cash payments may accompany share exchange.
*`NOOF`-Offers that are not supervised or regulated by an official entity and being offered by a party, for example a broker, usually at a discount price, for example broker offer, mini-tender, mini odd lot offer or third party offer.
*`CERT`-Non-US beneficial owner certification requirement for exchange of temporary to permanent notes.
*`ODLT`-Sale or purchase of odd-lots to/from the issuing company, initiated either by the holder of the security or through an offer made by the issuer.
*`OTHR`-Other event, use only when no other event type applies, for example, a new event type.
*`PARI`-Occurs when securities with different characteristics, for example, shares with different entitlements to dividend or voting rights, become identical in all respects, for example, pari-passu or assimilation. May be scheduled in advance, for example, shares resulting from a bonus may become fungible after a pre-set period of time, or may result from outside events, for example, merger, reorganisation, issue of supplementary tranches.
*`PCAL`-Securities are redeemed in part before their scheduled final maturity date. It is done without any pool factor reduction. The redemption is reflected in a debit of the face amount (FAMT).
*`PRED`-Securities are redeemed in part before their scheduled final maturity date. The redemption is reflected in a pool factor reduction. No movement of securities occurs.
*`PINK`-Interest payment, in any kind except cash, distributed to holders of an interest bearing asset.
*`PLAC`-Changes in the state of incorporation for US companies and changes in the place of incorporation for foreign companies. Where shares need to be registered following the incorporation change, the holder(s) may have to elect the registrar.
*`PDEF`-Also called partial defeasance. Issuer has money set aside to redeem a portion of an issue and the indenture states that the securities could be called earlier than the stated maturity.
*`PRIO`-Form of open or public offer where, due to a limited amount of securities available, priority is given to existing shareholders.
*`BPUT`-Early redemption of a security at the election of the holder subject to the terms and condition of the issue with no reduction in nominal value.
*`REDO`-Event by which the unit (currency and/or nominal) of a security is restated, for example, nominal/par value of security in a national currency is restated in another currency.
*`REMK`-Purchase and sale of remarketed preferred equities/bonds through the negotiation of interest rate between the issuers and the holders.
*`BIDS`-Repurchase offer / issuer bid / reverse rights. Offer to existing holders by the issuing company to repurchase its own securities. The objective of the offer is to reduce the number of outstanding securities.
*`SPLR`-Decrease in a company's number of outstanding equities without any change in the shareholder's equity or the aggregate market value at the time of the split. Equity price and nominal value are increased accordingly.
*`RHTS`-Offer to holders of a security to subscribe for additional securities via the distribution of an intermediate security. Both processes are included in the same event.
*`DVSC`-Dividend or interest paid in the form of scrip.
*`SHPR`-Corporate event pays shareholders an amount in cash issued from the shares premium reserve. It is similar to a dividend but with different tax implications.
*`SMAL`-Modification of the smallest negotiable unit of shares in order to obtain a new negotiable unit.
*`SOFF`-Distribution of securities issued by another company. The distributed securities may either be of a newly created or of an existing company. For example, spin-off, demerger, unbundling, divestment.
*`DVSE`-Dividend paid to shareholders in the form of equities of the issuing corporation.
*`SPLF`-Increase in a corporation's number of outstanding equities without any change in the shareholder's equity or the aggregate market value at the time of the split. Equity price and nominal value are reduced accordingly.
*`TREC`-Event related to tax reclaim activities.
*`TEND`-Offer made to holders by a third party, requesting them to sell (tender) or exchange their securities.
*`DLST`-Security is no longer able to comply with the listing requirements of a stock exchange and is removed from official board quotation.
*`SUSP`-Trading in the security has been suspended.
*`EXWA`-Option offered to holders to buy (call warrant) or to sell (put warrant) a specific amount of stock, cash, or commodity, at a predetermined price, during a predetermined period of time (which usually corresponds to the life of the issue).
*`WTRC`-Certification process for withholding tax reduction or exemption based on the tax status of the holder.
*`WRTH`-Booking out of valueless securities.
*`ACCU`-Funds related event in which the income (for example accumulation units) that accrues during an accounting period is retained within the fund instead of being paid away to investors. The retained income is nonetheless deemed to have been distributed to investors for tax purposes.
*`INFO`-Information provided by the issuer having no accounting/financial impact on the holder.
*`TNDP`-Taxable component on non-distributed proceeds, for example, Australian deemed income or US 871m income regulation.

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 4
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | ACTV |
| 2 | ATTI |
| 3 | BRUP |
| 4 | DFLT |
| 5 | BONU |
| 6 | EXRI |
| 7 | CAPD |
| 8 | CAPG |
| 9 | CAPI |
| 10 | DRCA |
| 11 | DVCA |
| 12 | CHAN |
| 13 | COOP |
| 14 | CLSA |
| 15 | CONS |
| 16 | CONV |
| 17 | CREV |
| 18 | DECR |
| 19 | DETI |
| 20 | DSCL |
| 21 | DVOP |
| 22 | DRIP |
| 23 | DRAW |
| 24 | DTCH |
| 25 | EXOF |
| 26 | REDM |
| 27 | MCAL |
| 28 | INCR |
| 29 | PPMT |
| 30 | INTR |
| 31 | RHDI |
| 32 | LIQU |
| 33 | EXTM |
| 34 | MRGR |
| 35 | NOOF |
| 36 | CERT |
| 37 | ODLT |
| 38 | OTHR |
| 39 | PARI |
| 40 | PCAL |
| 41 | PRED |
| 42 | PINK |
| 43 | PLAC |
| 44 | PDEF |
| 45 | PRIO |
| 46 | BPUT |
| 47 | REDO |
| 48 | REMK |
| 49 | BIDS |
| 50 | SPLR |
| 51 | RHTS |
| 52 | DVSC |
| 53 | SHPR |
| 54 | SMAL |
| 55 | SOFF |
| 56 | DVSE |
| 57 | SPLF |
| 58 | TREC |
| 59 | TEND |
| 60 | DLST |
| 61 | SUSP |
| 62 | EXWA |
| 63 | WTRC |
| 64 | WRTH |
| 65 | ACCU |
| 66 | INFO |
| 67 | TNDP |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
