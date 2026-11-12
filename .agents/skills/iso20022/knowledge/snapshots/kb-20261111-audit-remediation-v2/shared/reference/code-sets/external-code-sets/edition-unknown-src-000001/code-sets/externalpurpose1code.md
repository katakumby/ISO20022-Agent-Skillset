---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalPurpose1Code"]
code_set: "ExternalPurpose1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalPurpose1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalPurpose1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external purpose code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`BKDF`-Delayed draw funding. Certain issuers may utilize delayed draw loans whereby the lender is committed to fund cash within a specified period once a call is made by the issuer. The lender receives a fee for entering into such a commitment.
*`BKFE`-Bank loan fees. Cash activity related to specific bank loan fees, including (a) agent / assignment fees; (b) amendment fees; (c) commitment fees; (d) consent fees; (e) cost of carry fees; (f) delayed compensation fees; (g) facility fees; (h) fronting fees; (i) funding fees; (j) letter of credit assignment fees.
*`BKFM`-Bank loan funding memo. Net cash movement for the loan contract final notification when sent separately from the loan contract final notification instruction.
*`BKIP`-Accrued interest payments. Specific to bank loans.
*`BKPP`-Principal paydowns. Specific to bank loans
*`CBLK`-A Service that is settling money for a bulk of card transactions, while referring to a specific transaction file or other information like terminal ID, card acceptor ID or other transaction details.
*`CDCB`-Purchase of Goods and Services with additional Cash disbursement at the POI (Cashback).
*`CDCD`-ATM Cash Withdrawal in an unattended or Cash Advance in an attended environment (POI or bank counter).
*`CDCS`-ATM Cash Withdrawal in an unattended or Cash Advance in an attended environment (POI or bank counter) with surcharging.
*`CDDP`-A combined service which enables the card acceptor to perform an authorisation for a temporary amount and a completion for the final amount within a limited time frame. Deferred Payment is only available in the unattended environment. Examples where this service is widely used are unattended petrol pumps and phone booths.
*`CDOC`-A service which allows the card acceptor to effect a credit to a cardholder' account. Unlike a Merchant Refund, an Original Credit is not preceded by a card payment. This service is used for example for crediting winnings from gaming.
*`CDQC`-Purchase of Goods which are equivalent to cash like coupons in casinos.
*`ETUP`-Transaction is related to a Service that is first reserving money from a card account and then is loading an e-purse application by this amount.
*`FCOL`-A Service that is settling card transaction related fees between two parties.
*`MTUP`-A Service that is first reserving money from a card account and then is loading a prepaid mobile phone amount by this amount.
*`ACCT`-Transaction moves funds between 2 accounts of same account holder at the same bank.
*`CASH`-Transaction is a general cash management instruction.
*`COLL`-Transaction is a collection of funds initiated via a credit transfer or direct debit.
*`CSDB`-Transaction is related to cash disbursement.
*`DEPT`-Transaction is releted to a payment of deposit.
*`INTC`-Transaction is an intra-company payment, ie, a payment between two companies belonging to the same group.
*`INTP`-Transaction is a payment between two accounts belonging to the same party (intra-party payment), where party is a natural person (identified by a private ID, not organisation ID).
*`LIMA`-Bank initiated account transfer to support zero target balance management, pooling or sweeping.
*`NETT`-Transaction is related to a netting operation.
*`BFWD`-Cash collateral related to any securities traded out beyond 3 days which include treasury notes, JGBs and Gilts.
*`CCIR`-Cash Collateral related to a Cross Currency Interest Rate Swap, indicating the exchange of fixed interest payments in one currency for those in another.
*`CCPC`-Cash Collateral associated with an ISDA or Central Clearing Agreement that is covering the initial margin requirements for OTC trades clearing through a CCP.
*`CCPM`-Cash Collateral associated with an ISDA or Central Clearing Agreement that is covering the variation margin requirements for OTC trades clearing through a CCP.
*`CCSM`-CCP Segregated initial margin: Initial margin on OTC Derivatives cleared through a CCP that requires segregation.
*`CRDS`-Cash collateral related to trading of credit default swap.
*`CRPR`-Cash collateral related to a combination of various types of trades.
*`CRSP`-Cash collateral related to cash lending/borrowing; letter of Credit; signing of master agreement.
*`CRTL`-Cash collateral related to opening of a credit line before trading.
*`EQPT`-Cash collateral related to trading of equity option (Also known as stock options).
*`EQUS`-Cash collateral related to equity swap trades where the return of an equity is exchanged for either a fixed or a floating rate of interest.
*`EXPT`-Cash collateral related to trading of an exotic option for example a non-standard option.
*`EXTD`-Cash collateral related to trading of exchanged traded derivatives in general (Opposite to Over the Counter (OTC)).
*`FIXI`-Cash collateral related to a fixed income instrument
*`FWBC`-Cash collateral payment against a Master Forward Agreement (MFA) where the cash is held in a segregated account and is not available for use by the client. Includes any instruments with a forward settling date such TBAs, repurchase agreements and bond forwards
*`FWCC`-Cash collateral payment against a Master Forward Agreement (MFA) where the cash is owned and may be used by the client when returned. Includes any instruments with a forward settling date such TBAs, repurchase agreements and bond forwards
*`FWSB`-Any cash payment related to the collateral for a Master Agreement forward, which is segregated, and not available for use by the client. Example master agreement forwards include TBA, repo and Bond Forwards.
*`FWSC`-Any cash payment related to the collateral for a Master agreement forward, which is owned by the client and is available for use by the client when it is returned to them from the segregated account. Example master agreement forwards include TBA, repo and Bond Forwards.
*`MARG`-Daily margin on listed derivatives – not segregated as collateral associated with an FCM agreement. Examples include listed futures and options margin payments; premiums for listed options not covered in the MT54X message.
*`MBSB`-MBS Broker Owned Segregated (40Act/Dodd Frank) Cash Collateral - Any cash payment related to the collateral for a Mortgage Back Security, which is segregated, and not available for use by the client.
*`MBSC`-MBS Client Owned Cash Segregated (40Act/Dodd Frank) Cash Collateral - Any cash payment related to the collateral for a Mortgage Back Security, which is owned by the client and is available for use by the client when it is returned to them from the segregated account
*`MGCC`-Initial futures margin. Where such payment is owned by the client and is available for use by them on return
*`MGSC`-Margin Client Owned Segregated Cash Collateral - Any cash payment related to the collateral for initial futures margin, which is owned by the client and is available for use by the client when it is returned to them from the segregated account.
*`OCCC`-Client owned collateral identified as eligible for OCC pledging.
*`OPBC`-Cash collateral payment for OTC options associated with an FCM agreement. Where such payment is segregated and not available for use by the client
*`OPCC`-Cash collateral payment for OTC options associated with an FCM agreement. Where such payment is not segregated and is available for use by the client upon return
*`OPSB`-Option Broker Owned Segregated Cash Collateral - Any cash payment related to the collateral for an OTC option, which is segregated, and not available for use by the client.
*`OPSC`-Option Client Owned Cash Segregated Cash Collateral - Any cash payment related to the collateral for an OTC option, which is owned by the client and is available for use by the client when it is returned to them from the segregated account
*`OPTN`-Cash collateral related to trading of option on Foreign Exchange.
*`OTCD`-Cash collateral related to Over-the-counter (OTC) Derivatives in general for example contracts which are traded and privately negotiated.
*`REPO`-Cash collateral related to a repurchase agreement transaction.
*`RPBC`-Bi-lateral repo broker owned collateral associated with a repo master agreement – GMRA or MRA Master Repo Agreements.
*`RPCC`-Repo client owned collateral associated with a repo master agreement – GMRA or MRA Master Repo Agreements
*`RPSB`-Bi-lateral repo broker owned segregated cash collateral associated with a repo master agreement.
*`RPSC`-Repo client owned segregated collateral associated with a repo master agreement.
*`RVPO`-Cash collateral related to a reverse repurchase agreement transaction.
*`SBSC`-Cash collateral related to a Securities Buy Sell Sell Buy Back
*`SCIE`-Cash collateral related to Exotic single currency interest rate swap.
*`SCIR`-Cash collateral related to Single Currency Interest Rate Swap.
*`SCRP`-Cash collateral related to Combination of securities-related exposure types.
*`SHBC`-Short Sale broker owned collateral associated with a prime broker agreement.
*`SHCC`-Short Sale client owned collateral associated with a prime brokerage agreement.
*`SHSL`-Cash Collateral related to a Short Sell
*`SLEB`-Cash collateral related to Securities lending and borrowing.
*`SLOA`-Cash collateral related to a Secured loan.
*`SWBC`-Cash collateral payment for swaps associated with an ISDA agreement. . Where such payment is segregated and
not available for use by the client. Includes any cash collateral payments made under the terms of a CSA agreement
for instruments such as swaps and FX forwards.
*`SWCC`-Cash collateral payment for swaps associated with an ISDA agreement. Where such payment is not segregated and
is available for use by the client upon return. Includes any cash collateral payments made under the terms of a CSA
agreement for instruments such as swaps and FX forwards.
*`SWPT`-Cash collateral related to an option on interest rate swap.
*`SWSB`-Swaps Broker Owned Segregated Cash Collateral - Any cash payment related to the collateral for Swap margin ,
which is segregated, and not available for use by the client. This includes any collateral identified in a CSA
agreement such as Swap or FX Forward collateral.
*`SWSC`-Swaps Client Owned Segregated Cash Collateral - Any cash payment related to the collateral for Swap margin,
which is owned by the client and is available for use by the client when returned from the segregated account. This
includes any collateral identified in a CSA agreement such as Swap or FX Forward collateral.
*`TBAS`-Cash collateral related to a To Be Announced (TBA)
*`TBBC`-Cash collateral payment (segregated) for TBA securities associated with a TBA Master Agreement. Where such payment is segregated and not available for use by the client.
*`TBCC`-Cash collateral payment (for use by client)for TBA securities associated with a TBA Master Agreement. Where such payment is not segregated and is available for use by the client upon return.
*`TRCP`-Cash collateral related to a combination of treasury-related exposure types.
*`AGRT`-Transaction is related to the agricultural domain.
*`AREN`-Transaction is related to a payment associated with an Account Receivable Entry
*`BEXP`-Transaction is related to a payment of business expenses.
*`BOCE`-Transaction is related to a payment associated with a Back Office Conversion Entry
*`COMC`-Transaction is related to a payment of commercial credit or debit. (formerly CommercialCredit).
*`CPYR`-Transaction is payment of copyright.
*`GDDS`-Transaction is related to purchase and sale of goods.
*`GDSV`-Transaction is related to purchase and sale of goods and services.
*`GSCB`-Transaction is related to purchase and sale of goods and services with cash back.
*`LICF`-Transaction is payment of a license fee.
*`MP2B`-A service which enables a user to use an app on its mobile to pay a merchant or other business payees by initiating a payment message. Within this context, the account information or an alias of the payee might be transported through different channels to the app, for example QR Code, NFC, Bluetooth, other Networks.
*`POPE`-Transaction is related to a payment associated with a Point of Purchase Entry.
*`ROYA`-Transaction is the payment of royalties.
*`SCVE`-Transaction is related to purchase and sale of services.
*`SERV`-Transaction is related to service charges charged by a service provider.
*`SUBS`-Transaction is related to a payment of information or entertainment services either in printed or electronic form.
*`SUPP`-Transaction is related to a payment to a supplier.
*`TRAD`-Transaction is related to a trade services operation.
*`CHAR`-Transaction is a payment for charity reasons.
*`COMT`-Transaction is a payment used by a third party who can collect funds to pay on behalf of consumers, ie credit counseling or bill payment companies.
*`MP2P`-A service which enables a user to use an app on its mobile to initiate moving funds from his/her bank account to another person’s bank account while not using the account number  but an alias information like an MSISDN as account addressing information in his/her app.
*`ECPG`-E-Commerce payment with payment guarantee of the issuing bank.
*`ECPR`-E-Commerce payment return.
*`ECPU`-E-Commerce payment without payment guarantee of the issuing bank.
*`EPAY`-Transaction is related to ePayment.
*`CLPR`-Transaction is a payment of car loan principal payment.
*`COMP`-Transaction is related to the payment of a compensation relating to interest loss/value date adjustment and can include fees.
*`DBTC`-Collection of funds initiated via a debit transfer.
*`GOVI`-Transaction is related to a payment of government insurance.
*`HLRP`-Transaction is related to a payment of property loan.
*`HLST`-Transaction is related to the settlement of a property loan.
*`INPC`-Transaction is a payment of car insurance premium.
*`INPR`-Transaction is related to an insurance premium refund.
*`INSC`-Transaction is related to the payment of an insurance claim.
*`INSU`-Transaction is payment of an insurance premium.
*`INTE`-Transaction is payment of interest.
*`LBRI`-Transaction is a payment of labor insurance.
*`LIFI`-Transaction is a payment of life insurance.
*`LOAN`-Transaction is related to transfer of loan to borrower.
*`LOAR`-Transaction is related to repayment of loan to lender.
*`PENO`-Payment based on enforcement orders except those arising from judicial alimony decrees.
*`PPTI`-Transaction is a payment of property insurance.
*`RELG`-Transaction is for general rental/lease.
*`RINP`-Transaction is related to a payment of a recurring installment made at regular intervals.
*`TRFD`-Transaction is related to a payment of a trust fund.
*`FORW`-FX trades with a value date in the future.
*`FXNT`-FX netting if cash is moved by separate wire instead of within the closing FX instruction
*`ADMG`-Transaction is related to a payment associated with administrative management.
*`ADVA`-Transaction is an advance payment.
*`BCDM`-Transaction is the payment of a domestic bearer cheque.
*`BCFG`-Transaction is the payment of a foreign bearer cheque.
*`BLDM`-Transaction is related to a payment associated with building maintenance.
*`BNET`-Bond Forward pair-off cash net movement.
*`CBFF`-Transaction is related to capital building fringe fortune, ie capital building in general.
*`CBFR`-Transaction is related to capital building fringe fortune for retirement.
*`CCRD`-Transaction is related to a payment of credit card account.
*`CDBL`-Transaction is related to a payment of credit card bill.
*`CFEE`-Transaction is related to a payment of cancellation fee.
*`CGDD`-Transaction is related to a direct debit where the mandate was generated by using data from a payment card at the point of sale.
*`CORT`-Transaction is related to settlement of a trade, e.g. a foreign exchange deal or a securities transaction.
*`COST`-Transaction is related to payment of costs.
*`CPKC`-Transaction is related to carpark charges.
*`DCRD`-Transaction is related to a debit card payment.
*`DSMT`-Transaction is the payment of a disbursement due to a specific type of printed order for a payment of a  specified sum, issued by a bank or a post office (Zahlungsanweisung zur Verrechnung)
*`DVPM`-Code used to pre-advise the account servicer of a forthcoming deliver against payment instruction.
*`EDUC`-Transaction is related to a payment of study/tuition fees.
*`FACT`-Payment related to a factor update
*`FAND`-Financial aid by State authorities for abolition of consequences of natural disasters.
*`FCPM`-Transaction is the payment for late fees & charges. E.g Credit card charges
*`FEES`-Payment of fees/charges.
*`GIFT`-Payment with no commercial or statutory purpose.
*`GOVT`-Transaction is a payment to or from a government department.
*`ICCP`-Transaction is reimbursement of credit card payment.
*`IDCP`-Transaction is reimbursement of debit card payment.
*`IHRP`-Transaction is payment for an installment/hire-purchase agreement.
*`INSM`-Transaction is related to a payment of an installment.
*`IVPT`-Transaction is the payment for invoices.
*`MCDM`-Transaction is the payment of a domestic multi-currency cheque
*`MCFG`-Transaction is the payment of a foreign multi-currency cheque
*`MSVC`-Transaction is related to a payment for multiple service types.
*`NOWS`-Transaction is related to a payment for type of services not specified elsewhere.
*`OCDM`-Transaction is the payment of a domestic order cheque
*`OCFG`-Transaction is the payment of a foreign order cheque
*`OFEE`-Transaction is related to a payment of opening fee.
*`OTHR`-Other payment purpose.
*`PADD`-Transaction is related to a pre-authorized debit origination
*`PTSP`-Transaction is related to payment terms specifications
*`RCKE`-Transaction is related to a payment associated with a re-presented check entry
*`RCPT`-Transaction is related to a payment of receipt.
*`REBT`-Transaction is the payment of a rebate.
*`REFU`-Transaction is the payment of a refund.
*`RENT`-Transaction is the payment of rent.
*`REOD`-Transaction is for account overdraft repayment
*`RIMB`-Transaction is related to a reimbursement of a previous erroneous transaction.
*`RPNT`-Bi-lateral repo interest net/bulk payment at rollover/pair-off or other closing scenarios where applicable.
*`RRBN`-Cash payment resulting from a Round Robin
*`RRCT`-Transaction is related to a reimbursement for commercial reasons of a correctly received credit transfer.
*`RRTP`-Transaction is related to a Request to Pay.
*`RVPM`-Code used to pre-advise the account servicer of a forthcoming receive against payment instruction.
*`SLPI`-Transaction is payment of a well formatted payment slip.
*`SPLT`-Split payments. To be used when cash and security movements for a security trade settlement are instructed
separately.
*`STDY`-Transaction is related to a payment of study/tuition costs.
*`TBAN`-TBA pair-off cash wire net movement
*`TBIL`-Transaction is related to a payment of telecommunications related bill.
*`TCSC`-Transaction is related to a payment associated with charges levied by a town council.
*`TELI`-Transaction is related to a payment initiated via telephone.
*`TMPG`-Cash payment resulting from a TMPG Claim
*`TPRI`-Tri-Party Repo related interest
*`TPRP`-Tri-party Repo related net gain/loss cash movement
*`TRNC`-Transaction is payment of a beneficiary prefilled payment slip where beneficiary to payer information is truncated.
*`TRVC`-Transaction is the payment of a travellers cheque
*`WEBI`-Transaction is related to a payment initiated via internet.
*`IPAY`-Transaction in which the amount is available to the payee immediately.
*`IPCA`-Transaction in which the Return of the amount is fully returned.
*`IPDO`-Transaction in which the amount is available to the payee immediately, done for donations, with sending the address data of the payer.
*`IPEA`-Transaction in which the amount is available to the payee immediately, done in E-commerce, without sending the address data of the payer.
*`IPEC`-Transaction in which the amount is available to the payee immediately, done in E-commerce, with sending the address data of the payer.
*`IPEW`-Transaction in which the amount is available to the payee immediately, done in E-commerce.
*`IPPS`-Transaction in which the amount is available to the payee immediately, done at POS.
*`IPRT`-Transaction in which the Return of the amount is fully or partial returned.
*`IPU2`-Transaction is made via an unattending vending machine by using 2-factor-authentification.
*`IPUW`-Transaction is made via an unattending vending machine by without using 2-factor-authentification.
*`ANNI`-Transaction settles annuity related to credit, insurance, investments, other.n
*`CAFI`-Transaction is the payment of custodian account management fee where custodian bank and current account servicing bank coincide.
*`CFDI`-Transaction is the payment of capital falling due where custodian bank and current account servicing bank coincide.
*`CMDT`-Transaction is payment of commodities.
*`DERI`-Transaction is related to a derivatives transaction.
*`DIVD`-Transaction is payment of dividends.
*`FREX`-Transaction is related to a foreign exchange operation.
*`HEDG`-Transaction is related to a hedging operation.
*`INVS`-Transaction is for the payment of mutual funds, investment products and shares
*`PRME`-Transaction is related to a precious metal operation.
*`SAVG`-Transfer to / from savings or to retirement account.
*`SECU`-Transaction is the payment of securities.
*`SEPI`-Transaction is the payment of a purchase of securities where custodian bank and current account servicing bank coincide
*`TREA`-Transaction is related to treasury operations.
*`UNIT`-Transaction is purchase of Unit Trust
*`FNET`-Cash associated with a netting of futures payments. Refer to CCPM codeword for netting of initial and variation margin through a CCP
*`FUTR`-Cash related to futures trading activity.
*`ANTS`-Transaction is a payment for anesthesia services.
*`CVCF`-Transaction is a payment for convalescence care facility services.
*`DMEQ`-Transaction is a payment is for use of durable medical equipment.
*`DNTS`-Transaction is a payment for dental services.
*`HLTC`-Transaction is a payment for home health care services.
*`HLTI`-Transaction is a payment of health insurance.
*`HSPC`-Transaction is a payment for hospital care services.
*`ICRF`-Transaction is a payment for intermediate care facility services.
*`LTCF`-Transaction is a payment for long-term care facility services.
*`MAFC`-Transaction is contribution to medical aid fund.
*`MARF`-Transaction is related to a medical aid refund.
*`MDCS`-Transaction is a payment for medical care services.
*`VIEW`-Transaction is a payment for vision care services.
*`CDEP`-Payment related to a credit default event.
*`SWFP`-Final payments for a swap contract
*`SWPP`-Partial payment for a swap contract
*`SWRS`-Reset payment for a swap contract
*`SWUF`-Upfront payment for a swap contract
*`ADCS`-Payments for donation, sponsorship, advisory, intellectual and other copyright services.
*`AEMP`-Payment concerning active employment policy.
*`ALLW`-Transaction is the payment of allowances.
*`ALMY`-Transaction is the payment of alimony.
*`BBSC`-Transaction is related to a payment made as incentive to encourage parents to have more children
*`BECH`-Transaction is related to a payment made to assist parent/guardian to maintain child.
*`BENE`-Transaction is related to a payment to a person who is unemployed/disabled.
*`BONU`-Transaction is related to payment of a bonus.
*`CCHD`-Payments made by Government institute related to cash compensation, helplessness, disability. These payments are made by the Government institution as a social benefit in addition to regularly paid salary or pension.
*`COMM`-Transaction is payment of commission.
*`CSLP`-Transaction is a payment by a company to a bank for financing social loans to employees.
*`GFRP`-Compensation to unemployed persons during insolvency procedures.
*`GVEA`-Transaction is payment to category A Austrian government employees.
*`GVEB`-Transaction is payment to category B Austrian government employees.
*`GVEC`-Transaction is payment to category C Austrian government employees.
*`GVED`-Transaction is payment to category D Austrian government employees.
*`GWLT`-Payment to victims of war violence and to disabled soldiers.
*`HREC`-Transaction is a contribution by an employer to the housing expenditures (purchase, construction, renovation) of the employees within a tax free fringe benefit system.
*`PAYR`-Transaction is related to the payment of payroll.
*`PEFC`-Transaction is contribution to pension fund.
*`PENS`-Transaction is the payment of pension.
*`PRCP`-Transaction is related to a payment of a price.
*`RHBS`-Benefit for the duration of occupational rehabilitation.
*`SALA`-Transaction is the payment of salaries.
*`SPSP`-Salary or pension payment for more months in one amount or a delayed payment of salaries or pensions.
*`SSBE`-Transaction is a social security benefit, ie payment made by a government to support individuals.
*`LBIN`-Net payment related to a buy-in. When an investment manager is bought in on a sell trade that fails due to a failed securities lending recall, the IM may seize the underlying collateral to pay for the buy-in. Any difference between the value of the collateral and the sell proceeds would be paid or received under this code
*`LCOL`-Free movement of cash collateral. Cash collateral paid by the borrower is done separately from the delivery of the shares at loan opening or return of collateral done separately from return of the loaned security. Note: common when the currency of the security is different the currency of the cash collateral.
*`LFEE`-Fee payments, other than rebates, for securities lending. Includes (a) exclusive fees; (b) transaction fees; (c)
custodian fees; (d) minimum balance fees
*`LMEQ`-Cash collateral payments resulting from the marked-to-market of a portfolio of loaned equity securities
*`LMFI`-Cash collateral payments resulting from the marked-to-market of a portfolio of loaned fixed income securities
*`LMRK`-Cash collateral payments resulting from the marked-to-market of a portfolio of loaned securities where the instrument
types are not specified
*`LREB`-Securities lending rebate payments
*`LREV`-Revenue payments made by the lending agent to the client
*`LSFL`-Payments made by a borrower to a lending agent to satisfy claims made by the investment manager related to sell fails from late loan recall deliveries
*`ESTX`-Transaction is related to a payment of estate tax.
*`FWLV`-Transaction is related to a payment of Foreign Worker Levy
*`GSTX`-Transaction is the payment of Goods & Services Tax
*`HSTX`-Transaction is related to a payment of housing tax.
*`INTX`-Transaction is related to a payment of income tax.
*`NITX`-Transaction is related to a payment of net income tax.
*`PTXP`-Transaction is related to a payment of property tax.
*`RDTX`-Transaction is related to a payment of road tax.
*`TAXS`-Transaction is the payment of taxes.
*`VATX`-Transaction is the payment of value added tax.
*`WHLD`-Transaction is related to a payment of withholding tax.
*`TAXR`-Transaction is the refund of a tax payment or obligation.
*`B112`-US mutual fund trailer fee (12b-1) payment
*`BR12`-US mutual fund trailer fee (12b-1) rebate payment
*`TLRF`-Any non-US mutual fund trailer fee (retrocession) payment (use ISIN to determine onshore versus offshore designation)
*`TLRR`-Any non-US mutual fund trailer fee (retrocession) rebate payment (use ISIN to determine onshore versus offshore designation)
*`AIRB`-Transaction is a payment for air transport related business.
*`BUSB`-Transaction is a payment for bus transport related business.
*`FERB`-Transaction is a payment for ferry related business.
*`RLWY`-Transaction is a payment for railway transport related business.
*`TRPT`-Transaction is for the payment to top-up pre-paid card and electronic road pricing for the purpose of transportation
*`CBTV`-Transaction is related to a payment of cable TV bill.
*`ELEC`-Transaction is related to a payment of electricity bill.
*`ENRG`-Transaction is related to a utility operation.
*`GASB`-Transaction is related to a payment of gas bill.
*`NWCH`-Transaction is related to a payment of network charges.
*`NWCM`-Transaction is related to a payment of network communication.
*`OTLC`-Transaction is related to a payment of other telecom related bill.
*`PHON`-Transaction is related to a payment of telephone bill.
*`UBIL`-Transaction is for the payment to common utility provider that provide gas, water and/or electricity.
*`WTER`-Transaction is related to a payment of water bill.
*`BOND`-Securities Lending-Settlement of Bond transaction.
*`CABD`-Securities Lending-Settlement of Corporate Actions: Bonds transactions.
*`CAEQ`-Securities Lending-Settlement of Corporate Actions: Equities transactions.
*`CBCR`-Card Settlement-Settlement of Credit Card transactions.
*`DBCR`-Card Settlement-Settlement of Debit Card transactions.
*`DICL`-Card Settlement-Settlement of Diners transactions.
*`EQTS`-Securities Lending-Settlement of Equities transactions.
*`FLCR`-Card Settlement-Settlement of Fleet transactions.
*`EFTC`-Utilities-Settlement of Low value Credit transactions.
*`EFTD`-Utilities-Settlement of Low value Debit transactions.
*`MOMA`-Securities Lending-ettlement of Money Market PCH.
*`RAPI`-Instant Payments-Settlement of Rapid Payment Instruction (RPI) transactions.
*`GAMB`-General-Payments towards a purchase or winnings received from gambling, betting or other wagering activities.
*`LOTT`-General-Payment towards a purchase or winnings received from lottery activities.
*`AMEX`-Card Settlement-Settlement of AMEX transactions.
*`SASW`-Card Settlement-Settlement of ATM transactions.
*`AUCO`-Utilities-Settlement of Authenticated Collections transactions.
*`PCOM`-Final payment to complete the purchase of a property.
*`PDEP`-Payment of the deposit required towards purchase of a property.
*`PLDS`-Payment of funds from a lender as part of the issuance of a property loan.
*`PLRF`-Transfer or extension of a property financing arrangement to a new deal or loan provider, without change of ownership of property.
*`GAFA`-Salary and Benefits-Allowance from government to support family.
*`GAHO`-Salary and Benefits-Allowance from government to individuals to support payments of housing.
*`CPEN`-Cash penalties related to securities transaction, including CSDR Settlement Discipline Regime.
*`DEPD`-Transaction is related to a payment concerning dependent support, for example child support or support for a person substantially financially dependent on the support provider.
*`RETL`-Retail payment including e-commerce and online shopping.
*`DEBT`-Purpose of payment is the settlement of charges payable by the debtor in relation to an underlying customer credit transfer.
*`RMCO`-Utilities-Settlement of Unauthenticated Collections transactions.
*`INBC`-Settlement of charges in response to a prior interbank charge request.
*`LBXX`-Transaction is related to a cash transfer from an underlying fund to a holding collateralization account (ie. Longbox) for potential further use as collateral or back to the fund in case it is not required anymore.
*`MFSR`-Payment related to shares settlement of a subscription or redemption order.
*`CRYP`-Transaction is related to the purchase or sale of crypto assets.
*`MDEP`-Transaction is a small deposit, e.g., for account verification purposes.
*`BROK`-Account transfer funding a brokerage account.
*`ACTF`-Account transfer funding a bank account (Demand Deposit (DDA) and savings accounts).
*`WALM`-Account transfer funding a multi-use wallet.
*`WALS`-Account transfer funding a single purpose wallet.
*`CHDF`-Charitable donation being processed on behalf of a Donor Advised Fund (DAF).
*`CHFN`-Charitable donation being processed on behalf of a Foundation (purpose-driven entity).
*`CHCP`-Charitable donation being processed on behalf of a Corporate entity.
*`TNTP`-Transaction is a tax-neutral transfer of existing pension balance.
*`ALDS`-Disbursement of funds for vehicle purchases including cars, trucks, motorcycles, boats, RVs/motorhomes, ATVs/UTVs, jet skis, snowmobiles, commercial vehicles, and trailers.
*`PSDS`-Personal Loan Disbursement, e.g., disbursing funds for debt consolidation, home improvement, or major purchases.
*`BLDS`-Business Loan Disbursement, e.g., disbursing capital for business expansion, equipment purchase, or operational expenses.
*`SLDS`-Student Loan Disbursement, e.g., disbursing tuition funds to educational institutions or directly to students.
*`CLDS`-Construction Loan Disbursement, e.g., phased disbursements for construction projects based on completion milestones.
*`PDLN`-Pay Day Loan, e.g., short-term, high-interest loans typically due on borrower's next payday.
*`BNPL`-Buy Now Pay Later Payments, e.g., point-of-sale financing options allowing installment payments for retail purchases.
*`ESCR`-Financial intermediation services via an escrow account, e.g., real estate transactions, online marketplace purchases, business acquisitions, construction projects, legal settlements.
*`ODPY`-On demand/Real-time payments, e.g., Same-day wage access, gig economy payouts.
*`FUEL`-Fuel/Gas, e.g., purchases at gas stations for vehicle fuel or at charging stations for electric vehicles.
*`TOLL`-Tolls, e.g., payments for road tolls, bridges, tunnels, or electronic toll collection systems.
*`CARL`-Car Rentals, e.g., short-term vehicle rentals.
*`TRVL`-Generic code for travel and hospitality related transactions, e.g., hotel bookings, vacation rentals, travel packages, or direct hotel reservations.
*`GYMM`-Gym Membership, e.g., monthly or annual fees for fitness centers or health clubs.
*`HMMS`-Home Maintenance Related, e.g., regular services for home cleaning, lawn care, pest control, or pool maintenance.
*`STRM`-Streaming Services, e.g., monthly subscriptions to digital content platforms.
*`HRPS`-Home Repair, e.g., one-time or emergency repairs for washer/dryer, damaged floors, plumbing issues, or electrical problems.
*`RHSV`-Ride-hailing/Delivery Service, e.g., payments for app-based rides.
*`FGDL`-Food/Grocery Delivery, e.g., delivery fees and payments through app-based food delivery services.
*`ERPM`-Emergency relief payments, e.g., receiving assistance after natural disasters, COVID relief payments, or emergency aid disbursements.
*`GOVG`-Government Grants, e.g., receiving funds for academic research, small business development, educational programs, or community initiatives.
*`TIPS`-Tip/Gratuity, e.g., additional payments for service workers at restaurants, hotels, salons, or through digital tipping platforms.
*`SCAC`-Transaction is related to payment for school activities, extracurricular programs.
*`WALT`-Transaction is related to digital wallet funding or defunding.

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
| 1 | BKDF |
| 2 | BKFE |
| 3 | BKFM |
| 4 | BKIP |
| 5 | BKPP |
| 6 | CBLK |
| 7 | CDCB |
| 8 | CDCD |
| 9 | CDCS |
| 10 | CDDP |
| 11 | CDOC |
| 12 | CDQC |
| 13 | ETUP |
| 14 | FCOL |
| 15 | MTUP |
| 16 | ACCT |
| 17 | CASH |
| 18 | COLL |
| 19 | CSDB |
| 20 | DEPT |
| 21 | INTC |
| 22 | INTP |
| 23 | LIMA |
| 24 | NETT |
| 25 | BFWD |
| 26 | CCIR |
| 27 | CCPC |
| 28 | CCPM |
| 29 | CCSM |
| 30 | CRDS |
| 31 | CRPR |
| 32 | CRSP |
| 33 | CRTL |
| 34 | EQPT |
| 35 | EQUS |
| 36 | EXPT |
| 37 | EXTD |
| 38 | FIXI |
| 39 | FWBC |
| 40 | FWCC |
| 41 | FWSB |
| 42 | FWSC |
| 43 | MARG |
| 44 | MBSB |
| 45 | MBSC |
| 46 | MGCC |
| 47 | MGSC |
| 48 | OCCC |
| 49 | OPBC |
| 50 | OPCC |
| 51 | OPSB |
| 52 | OPSC |
| 53 | OPTN |
| 54 | OTCD |
| 55 | REPO |
| 56 | RPBC |
| 57 | RPCC |
| 58 | RPSB |
| 59 | RPSC |
| 60 | RVPO |
| 61 | SBSC |
| 62 | SCIE |
| 63 | SCIR |
| 64 | SCRP |
| 65 | SHBC |
| 66 | SHCC |
| 67 | SHSL |
| 68 | SLEB |
| 69 | SLOA |
| 70 | SWBC |
| 71 | SWCC |
| 72 | SWPT |
| 73 | SWSB |
| 74 | SWSC |
| 75 | TBAS |
| 76 | TBBC |
| 77 | TBCC |
| 78 | TRCP |
| 79 | AGRT |
| 80 | AREN |
| 81 | BEXP |
| 82 | BOCE |
| 83 | COMC |
| 84 | CPYR |
| 85 | GDDS |
| 86 | GDSV |
| 87 | GSCB |
| 88 | LICF |
| 89 | MP2B |
| 90 | POPE |
| 91 | ROYA |
| 92 | SCVE |
| 93 | SERV |
| 94 | SUBS |
| 95 | SUPP |
| 96 | TRAD |
| 97 | CHAR |
| 98 | COMT |
| 99 | MP2P |
| 100 | ECPG |
| 101 | ECPR |
| 102 | ECPU |
| 103 | EPAY |
| 104 | CLPR |
| 105 | COMP |
| 106 | DBTC |
| 107 | GOVI |
| 108 | HLRP |
| 109 | HLST |
| 110 | INPC |
| 111 | INPR |
| 112 | INSC |
| 113 | INSU |
| 114 | INTE |
| 115 | LBRI |
| 116 | LIFI |
| 117 | LOAN |
| 118 | LOAR |
| 119 | PENO |
| 120 | PPTI |
| 121 | RELG |
| 122 | RINP |
| 123 | TRFD |
| 124 | FORW |
| 125 | FXNT |
| 126 | ADMG |
| 127 | ADVA |
| 128 | BCDM |
| 129 | BCFG |
| 130 | BLDM |
| 131 | BNET |
| 132 | CBFF |
| 133 | CBFR |
| 134 | CCRD |
| 135 | CDBL |
| 136 | CFEE |
| 137 | CGDD |
| 138 | CORT |
| 139 | COST |
| 140 | CPKC |
| 141 | DCRD |
| 142 | DSMT |
| 143 | DVPM |
| 144 | EDUC |
| 145 | FACT |
| 146 | FAND |
| 147 | FCPM |
| 148 | FEES |
| 149 | GIFT |
| 150 | GOVT |
| 151 | ICCP |
| 152 | IDCP |
| 153 | IHRP |
| 154 | INSM |
| 155 | IVPT |
| 156 | MCDM |
| 157 | MCFG |
| 158 | MSVC |
| 159 | NOWS |
| 160 | OCDM |
| 161 | OCFG |
| 162 | OFEE |
| 163 | OTHR |
| 164 | PADD |
| 165 | PTSP |
| 166 | RCKE |
| 167 | RCPT |
| 168 | REBT |
| 169 | REFU |
| 170 | RENT |
| 171 | REOD |
| 172 | RIMB |
| 173 | RPNT |
| 174 | RRBN |
| 175 | RRCT |
| 176 | RRTP |
| 177 | RVPM |
| 178 | SLPI |
| 179 | SPLT |
| 180 | STDY |
| 181 | TBAN |
| 182 | TBIL |
| 183 | TCSC |
| 184 | TELI |
| 185 | TMPG |
| 186 | TPRI |
| 187 | TPRP |
| 188 | TRNC |
| 189 | TRVC |
| 190 | WEBI |
| 191 | IPAY |
| 192 | IPCA |
| 193 | IPDO |
| 194 | IPEA |
| 195 | IPEC |
| 196 | IPEW |
| 197 | IPPS |
| 198 | IPRT |
| 199 | IPU2 |
| 200 | IPUW |
| 201 | ANNI |
| 202 | CAFI |
| 203 | CFDI |
| 204 | CMDT |
| 205 | DERI |
| 206 | DIVD |
| 207 | FREX |
| 208 | HEDG |
| 209 | INVS |
| 210 | PRME |
| 211 | SAVG |
| 212 | SECU |
| 213 | SEPI |
| 214 | TREA |
| 215 | UNIT |
| 216 | FNET |
| 217 | FUTR |
| 218 | ANTS |
| 219 | CVCF |
| 220 | DMEQ |
| 221 | DNTS |
| 222 | HLTC |
| 223 | HLTI |
| 224 | HSPC |
| 225 | ICRF |
| 226 | LTCF |
| 227 | MAFC |
| 228 | MARF |
| 229 | MDCS |
| 230 | VIEW |
| 231 | CDEP |
| 232 | SWFP |
| 233 | SWPP |
| 234 | SWRS |
| 235 | SWUF |
| 236 | ADCS |
| 237 | AEMP |
| 238 | ALLW |
| 239 | ALMY |
| 240 | BBSC |
| 241 | BECH |
| 242 | BENE |
| 243 | BONU |
| 244 | CCHD |
| 245 | COMM |
| 246 | CSLP |
| 247 | GFRP |
| 248 | GVEA |
| 249 | GVEB |
| 250 | GVEC |
| 251 | GVED |
| 252 | GWLT |
| 253 | HREC |
| 254 | PAYR |
| 255 | PEFC |
| 256 | PENS |
| 257 | PRCP |
| 258 | RHBS |
| 259 | SALA |
| 260 | SPSP |
| 261 | SSBE |
| 262 | LBIN |
| 263 | LCOL |
| 264 | LFEE |
| 265 | LMEQ |
| 266 | LMFI |
| 267 | LMRK |
| 268 | LREB |
| 269 | LREV |
| 270 | LSFL |
| 271 | ESTX |
| 272 | FWLV |
| 273 | GSTX |
| 274 | HSTX |
| 275 | INTX |
| 276 | NITX |
| 277 | PTXP |
| 278 | RDTX |
| 279 | TAXS |
| 280 | VATX |
| 281 | WHLD |
| 282 | TAXR |
| 283 | B112 |
| 284 | BR12 |
| 285 | TLRF |
| 286 | TLRR |
| 287 | AIRB |
| 288 | BUSB |
| 289 | FERB |
| 290 | RLWY |
| 291 | TRPT |
| 292 | CBTV |
| 293 | ELEC |
| 294 | ENRG |
| 295 | GASB |
| 296 | NWCH |
| 297 | NWCM |
| 298 | OTLC |
| 299 | PHON |
| 300 | UBIL |
| 301 | WTER |
| 302 | BOND |
| 303 | CABD |
| 304 | CAEQ |
| 305 | CBCR |
| 306 | DBCR |
| 307 | DICL |
| 308 | EQTS |
| 309 | FLCR |
| 310 | EFTC |
| 311 | EFTD |
| 312 | MOMA |
| 313 | RAPI |
| 314 | GAMB |
| 315 | LOTT |
| 316 | AMEX |
| 317 | SASW |
| 318 | AUCO |
| 319 | PCOM |
| 320 | PDEP |
| 321 | PLDS |
| 322 | PLRF |
| 323 | GAFA |
| 324 | GAHO |
| 325 | CPEN |
| 326 | DEPD |
| 327 | RETL |
| 328 | DEBT |
| 329 | RMCO |
| 330 | INBC |
| 331 | LBXX |
| 332 | MFSR |
| 333 | CRYP |
| 334 | MDEP |
| 335 | BROK |
| 336 | ACTF |
| 337 | WALM |
| 338 | WALS |
| 339 | CHDF |
| 340 | CHFN |
| 341 | CHCP |
| 342 | TNTP |
| 343 | ALDS |
| 344 | PSDS |
| 345 | BLDS |
| 346 | SLDS |
| 347 | CLDS |
| 348 | PDLN |
| 349 | BNPL |
| 350 | ESCR |
| 351 | ODPY |
| 352 | FUEL |
| 353 | TOLL |
| 354 | CARL |
| 355 | TRVL |
| 356 | GYMM |
| 357 | HMMS |
| 358 | STRM |
| 359 | HRPS |
| 360 | RHSV |
| 361 | FGDL |
| 362 | ERPM |
| 363 | GOVG |
| 364 | TIPS |
| 365 | SCAC |
| 366 | WALT |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
